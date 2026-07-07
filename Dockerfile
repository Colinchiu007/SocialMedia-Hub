# SocialMedia-Hub Dockerfile
# Multi-stage build for optimized image size

# Build stage
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies
RUN pip install --no-cache-dir hatchling

# Copy project files
COPY pyproject.toml .
COPY src/ src/

# Install dependencies
RUN pip install --no-cache-dir -e ".[server]"

# Runtime stage
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY src/ src/
COPY pyproject.toml .

# Set environment variables
ENV PYTHONPATH=/app/src
ENV SMH_HOST=0.0.0.0
ENV SMH_PORT=8000

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/api/v1/health/check || exit 1

# Run the application
CMD ["smh-server", "start", "--host", "0.0.0.0", "--port", "8000"]
