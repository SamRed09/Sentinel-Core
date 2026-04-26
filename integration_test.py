import subprocess
import socket
import psycopg2
import google.generativeai as genai
import datetime

# ==========================================
#  1. AI CORE CONFIGURATION
# ==========================================
API_KEY = "AIzaSyCVNYO8ILpXijB22VeNFRNpgV2IChOSXlc"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# ==========================================
# 2. DATABASE CONFIGURATION
# ==========================================
DB_HOST = "localhost"
DB_NAME = "sentinel_db"
DB_USER = "postgres"
DB_PASS = "secret"

def get_ai_remediation(error_message):
    print("🧠 Violation detected. Asking AI for remediation...")
    prompt = f"""
    You are a Linux Security Expert. I have a compliance violation.
    Translate this error into a single, executable Ubuntu terminal command to fix it. 
    Respond ONLY with the terminal command.
    Error: {error_message}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def run_audit():
    hostname = socket.gethostname()
    check_name = "UFW Firewall Status"
    status = "True"
    ai_remediation = "System secure. No action required."

    print(f"🛡️ Sentinel Agent running on {hostname}...")
    
    # 🔍 3. RUN THE SECURITY SCAN
    try:
        # Check UFW status
        result = subprocess.run(['ufw', 'status'], capture_output=True, text=True)
        
        if "inactive" in result.stdout.lower():
            status = "False"
            # 🚨 Violation found! Trigger the AI Brain
            ai_remediation = get_ai_remediation("UFW firewall is inactive and needs to be enabled.")
            
    except Exception as e:
        status = "False"
        ai_remediation = f"Agent Error: Could not run scan. {str(e)}"

    #  4. PUSH TO DATABASE
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
        cur = conn.cursor()
        
        query = """
            INSERT INTO audit_logs (hostname, check_name, status, ai_remediation)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (hostname, check_name, status, ai_remediation))
        conn.commit()
        
        cur.close()
        conn.close()
        
        print("-" * 50)
        print(f" Status: {status}")
        print(f"🟢 AI Fix: {ai_remediation}")
        print(" Successfully pushed to Sentinel Core Database.")
        print("-" * 50)
        
    except Exception as e:
        print(f" Database Connection Error: {e}")

if __name__ == "__main__":
    run_audit()
