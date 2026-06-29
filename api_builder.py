import os
from typing import Dict, Any, Optional

class APIBuilderClient:
    """
    Client SDK to parse API spec documents and write client wrappers.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("API_BUILDER_API_KEY")
        self.mock_mode = self.api_key is None or self.api_key == "mock"

    def build_client(self, api_spec: str, default_timeout: int) -> str:
        """
        Parses endpoint info from text spec and outputs complete runnable code.
        """
        # Simple extraction logic for demo
        import re
        endpoint_match = re.search(r'(POST|GET)\s+(/\S+)', api_spec)
        method = endpoint_match.group(1) if endpoint_match else "POST"
        path = endpoint_match.group(2) if endpoint_match else "/v1/data"
        
        # Structure python class wrapper
        code_template = f"""import requests
import time

class CustomAPIClient:
    def __init__(self, base_url="https://api.example.com", token=None):
        self.base_url = base_url.rstrip('/')
        self.headers = {{"Authorization": f"Bearer {{token}}"}} if token else {{}}
        self.timeout = {default_timeout}

    def execute_request(self, payload=None):
        url = f"{{self.base_url}}{path}"
        for attempt in range(3):
            try:
                if "{method}" == "POST":
                    resp = requests.post(url, json=payload, headers=self.headers, timeout=self.timeout)
                else:
                    resp = requests.get(url, params=payload, headers=self.headers, timeout=self.timeout)
                resp.raise_for_status()
                return resp.json()
            except Exception as e:
                if attempt == 2:
                    raise e
                time.sleep(2 ** attempt)
"""
        return code_template.strip()
