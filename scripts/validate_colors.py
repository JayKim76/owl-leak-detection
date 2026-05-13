import json
import sys

def validate_brand_colors(token_path, target_color):
    with open(token_path, 'r') as f:
        tokens = json.load(f)
    
    allowed_colors = set(tokens['colors'].values())
    
    if target_color in allowed_colors:
        print(f"✅ Success: '{target_color}' is a valid Datasys brand color.")
        return True
    else:
        print(f"❌ Error: '{target_color}' is NOT an approved brand color!")
        print(f"Allowed colors: {allowed_colors}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_colors.py <hex_color>")
        sys.exit(1)
    
    test_color = sys.argv[1]
    token_file = 'src/design/tokens.json'
    
    if not validate_brand_colors(token_file, test_color):
        sys.exit(1)