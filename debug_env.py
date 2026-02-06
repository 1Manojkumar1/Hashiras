import os
from dotenv import load_dotenv

load_dotenv()

with open("debug_output.txt", "w", encoding="utf-8") as out:
    def log(msg):
        print(msg)
        out.write(msg + "\n")

    log("--- ENV DEBUG DIAGNOSTIC ---")
    keys_to_check = ["OPENROUTER_API_KEY", "SYLLABUS_API_KEY", "RESOURCE_API_KEY", "GAP_API_KEY"]
    invalid_values = ["your_key_here", "your_openrouter_api_key_here", ""]

    for key in keys_to_check:
        val = os.getenv(key)
        if val is None:
            log(f"❌ {key}: NOT FOUND in environment")
        elif val in invalid_values:
            log(f"⚠️ {key}: Found but matches placeholder '{val}'")
        else:
            val = val.strip()
            masked = val[:4] + "..." + val[-4:] if len(val) > 8 else "****"
            log(f"✅ {key}: Loaded successfully (Example: {masked}, Length: {len(val)})")
            if " " in val:
                 log(f"⚠️ {key}: WARNING - Value contains spaces")

    # Check if .env file exists
    if os.path.exists(".env"):
        log(f"\n✅ .env file exists at: {os.path.abspath('.env')}")
        try:
            with open(".env", "r") as f:
                lines = f.readlines()
                log(f"\n.env file has {len(lines)} lines.")
                for i, line in enumerate(lines):
                    if "API_KEY" in line:
                        clean_line = line.strip()
                        if "#" in clean_line and not clean_line.startswith("#"):
                            log(f"⚠️ Line {i+1} has inline comment: {clean_line.split('=')[0]}=...")
                        if " = " in clean_line:
                            log(f"⚠️ Line {i+1} has spaces around '=': {clean_line}")
                        
        except Exception as e:
            log(f"Error reading .env file: {e}")
    else:
        log(f"\n❌ .env file NOT FOUND at: {os.path.abspath('.env')}")
