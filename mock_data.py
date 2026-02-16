import psycopg2
import random
import time
from datetime import datetime

# Connect to your local database
# NOTE: We set the password to 'secret' in the previous step. 
try:
    conn = psycopg2.connect(
        dbname="sentinel_db",
        user="postgres",
        password="secret",
        host="localhost"
    )
    conn.autocommit = True
    cur = conn.cursor()
    print("✅ Connected to Database!")
except Exception as e:
    print(f"❌ Connection Failed: {e}")
    exit()

# The "Menu" of checks we are simulating
targets = ["Windows-Server-2019", "Ubuntu-Server-22"]
controls = [
    ("NCA-ECC-1-1", "Firewall Status"),
    ("NCA-ECC-1-5", "SSH Root Login Disabled"),
    ("NCA-ECC-2-1", "Antivirus Active"),
    ("NCA-ECC-3-4", "Password Complexity"),
    ("NCA-ECC-4-1", "System Patch Level")
]

print("🚀 Sentinel Ghost Generator is Running... (Press Ctrl+C to stop)")

while True:
    # Pick a random target and control
    target = random.choice(targets)
    control_id, check_name = random.choice(controls)

    # 80% chance of PASS, 20% chance of FAIL
    status = random.choice([True, True, True, True, False])

    # Generate a fake message based on status
    if status:
        msg = "Compliant: Settings match NCA standards."
    else:
        msg = "VIOLATION: Critical security mismatch detected!"

    # SQL Injection (The good kind)
    sql = """
        INSERT INTO audit_logs (hostname, control_id, check_name, status, message)
        VALUES (%s, %s, %s, %s, %s)
    """
    cur.execute(sql, (target, control_id, check_name, status, msg))

    current_time = datetime.now().strftime("%H:%M:%S")
    status_icon = "🟢" if status else "🔴"
    print(f"[{current_time}] {status_icon} {target} : {check_name}")

    # Wait 2 seconds before the next log
    time.sleep(2)

