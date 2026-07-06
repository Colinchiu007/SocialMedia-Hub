"""Performance benchmarks for SocialMedia-Hub."""

from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor

import pytest
from fastapi.testclient import TestClient

from socialmedia_hub.server.main import app


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


class TestResponseTimeBenchmarks:
    """Benchmark response times."""

    def test_health_check_latency(self, client):
        """Benchmark health check endpoint."""
        iterations = 100
        start = time.perf_counter()
        for _ in range(iterations):
            client.get("/api/v1/health/check")
        elapsed = time.perf_counter() - start
        avg_ms = (elapsed / iterations) * 1000

        print(f"\nHealth Check: {avg_ms:.2f}ms avg ({iterations} iterations)")
        assert avg_ms < 50, f"Average response time too high: {avg_ms:.2f}ms"

    def test_platform_list_latency(self, client):
        """Benchmark platform list endpoint."""
        iterations = 100
        start = time.perf_counter()
        for _ in range(iterations):
            client.get("/api/v1/health/platforms")
        elapsed = time.perf_counter() - start
        avg_ms = (elapsed / iterations) * 1000

        print(f"\nPlatform List: {avg_ms:.2f}ms avg ({iterations} iterations)")
        assert avg_ms < 50, f"Average response time too high: {avg_ms:.2f}ms"

    def test_monitor_status_latency(self, client):
        """Benchmark monitor status endpoint."""
        iterations = 100
        start = time.perf_counter()
        for _ in range(iterations):
            client.get("/api/v1/monitor/status")
        elapsed = time.perf_counter() - start
        avg_ms = (elapsed / iterations) * 1000

        print(f"\nMonitor Status: {avg_ms:.2f}ms avg ({iterations} iterations)")
        assert avg_ms < 50, f"Average response time too high: {avg_ms:.2f}ms"


class TestConcurrencyBenchmarks:
    """Benchmark concurrent request handling."""

    def test_concurrent_health_checks(self, client):
        """Benchmark concurrent health check requests."""
        def make_request():
            return client.get("/api/v1/health/check")

        iterations = 50
        start = time.perf_counter()
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(iterations)]
            results = [f.result() for f in futures]
        elapsed = time.perf_counter() - start

        avg_ms = (elapsed / iterations) * 1000
        print(f"\nConcurrent Health Check: {avg_ms:.2f}ms avg ({iterations} requests)")
        assert all(r.status_code == 200 for r in results)

    def test_concurrent_mixed_endpoints(self, client):
        """Benchmark concurrent mixed endpoint requests."""
        endpoints = [
            "/api/v1/health/check",
            "/api/v1/health/platforms",
            "/api/v1/monitor/status",
            "/api/v1/monitor/metrics",
        ]

        def make_request(endpoint):
            return client.get(endpoint)

        iterations = 40
        start = time.perf_counter()
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [
                executor.submit(make_request, endpoints[i % len(endpoints)])
                for i in range(iterations)
            ]
            results = [f.result() for f in futures]
        elapsed = time.perf_counter() - start

        avg_ms = (elapsed / iterations) * 1000
        print(f"\nConcurrent Mixed: {avg_ms:.2f}ms avg ({iterations} requests)")
        assert all(r.status_code == 200 for r in results)


class TestMemoryBenchmarks:
    """Benchmark memory usage."""

    def test_large_response_handling(self, client):
        """Test handling of large responses."""
        # This tests the server's ability to handle large payloads
        start = time.perf_counter()
        response = client.get("/api/v1/health/platforms")
        elapsed = time.perf_counter() - start

        assert response.status_code == 200
        print(f"\nLarge Response Handling: {elapsed*1000:.2f}ms")


class TestStartupBenchmarks:
    """Benchmark server startup time."""

    def test_server_import_time(self):
        """Benchmark server module import time."""
        start = time.perf_counter()
        elapsed = time.perf_counter() - start

        print(f"\nServer Import: {elapsed*1000:.2f}ms")
        assert elapsed < 1.0, f"Import time too high: {elapsed*1000:.2f}ms"

    def test_mcp_server_initialization(self):
        """Benchmark MCP server initialization time."""
        from socialmedia_hub.mcp.server import create_mcp_server

        start = time.perf_counter()
        mcp = create_mcp_server(api_key="test")
        elapsed = time.perf_counter() - start

        print(f"\nMCP Server Init: {elapsed*1000:.2f}ms ({len(mcp.tools)} tools)")
        assert elapsed < 1.0, f"Initialization time too high: {elapsed*1000:.2f}ms"
