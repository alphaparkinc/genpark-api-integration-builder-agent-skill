import sys
from api_builder import APIBuilderClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== API Integration Builder Agent Example ===")
    client = APIBuilderClient()
    
    spec = (
        "# User Validation Endpoint\n"
        "POST /v2/user/validate\n"
        "Headers:\n"
        "  Content-Type: application/json\n"
    )
    
    code = client.build_client(spec, default_timeout=15)
    print("\n--- Generated Python Client Code ---")
    print(code)

if __name__ == "__main__":
    main()
