"""Generate routes from OpenAPI spec."""

import json
from pathlib import Path
from typing import Any

SPEC_PATH = Path(r"D:\Data\MimoCode\TikHub-API-Python-SDK\spec\openapi.json")
ROUTES_DIR = Path(r"D:\Data\MimoCode\SocialMedia-Hub\src\socialmedia_hub\server\routes")

# Tag to router prefix mapping
TAG_PREFIX: dict[str, str] = {
    "Douyin-Web-API": "douyin/web",
    "Douyin-App-V3-API": "douyin/app/v3",
    "Douyin-Billboard-API": "douyin/billboard",
    "Douyin-Search-API": "douyin/search",
    "Douyin-Creator-API": "douyin/creator/v1",
    "Douyin-Creator-V2-API": "douyin/creator/v2",
    "Douyin-Xingtu-API": "douyin/xingtu/v1",
    "Douyin-Xingtu-V2-API": "douyin/xingtu/v2",
    "TikTok-Web-API": "tiktok/web",
    "TikTok-App-V3-API": "tiktok/app/v3",
    "TikTok-Ads-API": "tiktok/ads",
    "TikTok-Shop-Web-API": "tiktok/shop",
    "TikTok-Creator-API": "tiktok/creator",
    "TikTok-Interaction-API": "tiktok/interaction",
    "TikTok-Analytics-API": "tiktok/analytics",
    "Bilibili-Web-API": "bilibili/web",
    "Bilibili-App-API": "bilibili/app",
    "Instagram-V1-API": "instagram/v1",
    "Instagram-V2-API": "instagram/v2",
    "Instagram-V3-API": "instagram/v3",
    "YouTube-Web-API": "youtube/web",
    "YouTube-Web-V2-API": "youtube/web/v2",
    "Twitter-Web-API": "twitter/web",
    "Xiaohongshu-Web-API": "xiaohongshu/web",
    "Xiaohongshu-Web-V2-API": "xiaohongshu/web/v2",
    "Xiaohongshu-Web-V3-API": "xiaohongshu/web/v3",
    "Xiaohongshu-App-API": "xiaohongshu/app",
    "Xiaohongshu-App-V2-API": "xiaohongshu/app/v2",
    "Weibo-Web-API": "weibo/web",
    "Weibo-Web-V2-API": "weibo/web/v2",
    "Weibo-App-API": "weibo/app",
    "Kuaishou-Web-API": "kuaishou/web",
    "Kuaishou-App-API": "kuaishou/app",
    "LinkedIn-Web-API": "linkedin/web",
    "Reddit-APP-API": "reddit/app",
    "Zhihu-Web-API": "zhihu/web",
    "Threads-Web-API": "threads/web",
    "WeChat-Channels-API": "wechat/channels",
    "WeChat-Media-Platform-Web-API": "wechat/media",
    "Lemon8-App-API": "lemon8/app",
    "PiPiXia-App-API": "pipixia/app",
    "Sora2-API": "sora2",
    "Xigua-App-V2-API": "xigua/app/v2",
    "Toutiao-Web-API": "toutiao/web",
    "Toutiao-App-API": "toutiao/app",
    "TikHub-User-API": "tikhub/user",
    "TikHub-Downloader-API": "tikhub/downloader",
    "Temp-Mail-API": "temp_mail",
    "Hybrid-Parsing": "hybrid",
    "iOS-Shortcut": "ios_shortcut",
    "Demo-API": "demo",
}

# Method name to Python function name
def method_name(path: str) -> str:
    """Convert API path to Python function name."""
    parts = path.strip("/").split("/")
    # Get the last part as the base name
    name = parts[-1]
    # Clean up the name
    name = name.replace("-", "_")
    return name


def generate_route_file(tag: str, prefix: str, operations: list[dict[str, Any]]) -> str:
    """Generate a route file for a tag."""
    lines = [
        f'"""Auto-generated routes for {tag}."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from fastapi import APIRouter, Depends, Request",
        "",
        "from socialmedia_hub.server._core import proxy_request, verify_api_key",
        "",
        f'router = APIRouter(prefix="/api/v1/{prefix}", tags=["{tag.lower().replace("-", "_").replace("_api", "")}"])',
        "",
    ]

    for op in operations:
        path = op["path"]
        method = op["method"].upper()
        func_name = method_name(path)
        summary = op.get("summary", f"{method} {path}")
        params = [p for p in op.get("parameters", []) if p.get("in") == "query"]
        has_body = "requestBody" in op

        # Build function signature
        required_parts = []
        optional_parts = []
        for p in params:
            name = p["name"].replace("-", "_")
            required = p.get("required", False)
            schema = p.get("schema", {})
            ptype = "str"
            if schema.get("type") == "integer":
                ptype = "int"
            elif schema.get("type") == "number":
                ptype = "float"
            elif schema.get("type") == "boolean":
                ptype = "bool"

            if required:
                required_parts.append(f"    {name}: {ptype}")
            else:
                optional_parts.append(f"    {name}: {ptype} | None = None")

        # Add request parameter if has_body (before optional params)
        sig_parts = required_parts[:]
        if has_body:
            sig_parts.append("    request: Request")
        sig_parts.extend(optional_parts)
        sig_parts.append("    token: str = Depends(verify_api_key)")
        sig = ",\n".join(sig_parts)

        # Build function body
        body_lines = []
        # Only add request.json() for POST requests with body
        if has_body and method == "POST":
            body_lines.append("        body = await request.json()")
            if params:
                body_lines.append("        params: dict[str, Any] = {}")
                for p in params:
                    name = p["name"].replace("-", "_")
                    body_lines.append(f'        if {name} is not None:')
                    body_lines.append(f'            params["{p["name"]}"] = {name}')
                body_lines.append(f'        return await proxy_request("{prefix.split("/")[0]}", "{path}", params=params, json_body=body)')
            else:
                body_lines.append(f'        return await proxy_request("{prefix.split("/")[0]}", "{path}", json_body=body)')
        else:
            if params:
                body_lines.append("        params: dict[str, Any] = {}")
                for p in params:
                    name = p["name"].replace("-", "_")
                    body_lines.append(f'        if {name} is not None:')
                    body_lines.append(f'            params["{p["name"]}"] = {name}')
                body_lines.append(f'        return await proxy_request("{prefix.split("/")[0]}", "{path}", params=params)')
            else:
                body_lines.append(f'        return await proxy_request("{prefix.split("/")[0]}", "{path}")')

        # Generate the route
        http_method = "get" if method == "GET" else "post"
        route_path = "/" + path.split("/")[-1]
        lines.append(f'@router.{http_method}("{route_path}")')
        lines.append(f"async def {func_name}(")
        lines.append(sig)
        lines.append(") -> dict[str, Any]:")
        lines.append(f'    """{summary}"""')
        # Fix indentation: body should have 8 spaces (2 levels)
        fixed_body = [line.replace("        ", "    ", 1) if line.startswith("        ") else line for line in body_lines]
        lines.extend(fixed_body)
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    """Generate all route files from spec."""
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))

    # Group operations by tag
    tag_ops: dict[str, list[dict[str, Any]]] = {}
    for path, methods in spec["paths"].items():
        for http_method, op in methods.items():
            if http_method.lower() not in ("get", "post"):
                continue
            for tag in op.get("tags", ["_untagged"]):
                if tag not in tag_ops:
                    tag_ops[tag] = []
                tag_ops[tag].append({
                    "path": path,
                    "method": http_method,
                    "summary": op.get("summary", ""),
                    "parameters": op.get("parameters", []),
                    "requestBody": op.get("requestBody"),
                })

    # Generate files for tags with prefixes
    for tag, prefix in TAG_PREFIX.items():
        if tag not in tag_ops:
            continue
        ops = tag_ops[tag]
        content = generate_route_file(tag, prefix, ops)
        filename = f"auto_{prefix.replace('/', '_')}.py"
        filepath = ROUTES_DIR / filename
        filepath.write_text(content, encoding="utf-8")
        print(f"Generated {filepath.name} ({len(ops)} endpoints)")


if __name__ == "__main__":
    main()
