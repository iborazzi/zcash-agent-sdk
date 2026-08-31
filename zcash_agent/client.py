import requests
from typing import Dict, Any

class ZcashAgentClient:
    """Lightweight Zcash RPC & Node Wrapper for Agent Workflows."""
    
    def __init__(self, rpc_url: str = "http://127.0.0.1:8232", rpc_user: str = "", rpc_password: str = ""):
        self.rpc_url = rpc_url
        self.auth = (rpc_user, rpc_password) if rpc_user else None

    def _call_rpc(self, method: str, params: list = []) -> Dict[str, Any]:
        payload = {
            "jsonrpc": "1.0",
            "id": "agent-sdk",
            "method": method,
            "params": params
        }
        try:
            response = requests.post(self.rpc_url, json=payload, auth=self.auth, timeout=5)
            return response.json()
        except Exception as e:
            return {"error": str(e), "status": "failed"}

    def get_blockchain_info(self) -> Dict[str, Any]:
        """Check node connection and chain status."""
        return self._call_rpc("getblockchaininfo")

    def parse_unified_address(self, address: str) -> bool:
        """Validate Zcash Unified Address (UA) prefix."""
        return address.startswith("u1")
