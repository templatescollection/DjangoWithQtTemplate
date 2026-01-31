import sys

import requests  # type: ignore[import-untyped]

try:
    # Attempt to access the health endpoint
    response = requests.get("http://localhost:8000/", timeout=5)

    # Fail for 4xx/5xx status codes
    response.raise_for_status()
    sys.exit(0)  # Success exit code
except requests.RequestException as e:
    sys.stderr.write(f"Health check failed: {e!s}\n")
    sys.exit(1)  # Failure exit code
