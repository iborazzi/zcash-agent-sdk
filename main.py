from zcash_agent.client import ZcashAgentClient

def main():
    print("⚡ Initializing Zcash Agent SDK...")
    client = ZcashAgentClient()
    
    # Test Unified Address validation
    test_ua = "u1testaddress123456789"
    is_valid = client.parse_unified_address(test_ua)
    print(f"Address check for {test_ua}: Valid UA = {is_valid}")

if __name__ == "__main__":
    main()
