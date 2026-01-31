# Stage 1: Base build stage
FROM python:3.13-slim AS builder

LABEL maintainer="pouralijan.ir"

# Create the app directory
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies first for caching benefit
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# This for checkhealth
RUN pip install requests

# Stage 2: Production stage
FROM python:3.13-slim

LABEL maintainer="pouralijan.ir"

RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory
WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser . .
COPY --chown=appuser:appuser checkhealth.py /checkhealth.py
# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 8000

# Make entry file executable
RUN chmod +x  /app/entrypoint.prod.sh
# Set healthcheck command
HEALTHCHECK --interval=10s --timeout=5s --retries=5 CMD ["python", "/checkhealth.py"]
# Start the application using Gunicorn
RUN python manage.py collectstatic --noinput
CMD ["/app/entrypoint.prod.sh"]
