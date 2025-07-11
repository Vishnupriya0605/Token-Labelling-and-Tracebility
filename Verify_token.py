import sqlite3
from datetime import datetime


conn = sqlite3.connect("tokendata.db")
cursor = conn.cursor()


token_id = input("Enter scanned Token ID: ")


cursor.execute("SELECT * FROM tokens WHERE token_id = ?", (token_id,))
data = cursor.fetchone()

if data:
    issue_date, expiry_date, is_authorized = data[1], data[2], data[3]

    print(f"\nToken ID: {token_id}")
    print(f"Issue Date: {issue_date}")
    print(f"Expiry Date: {expiry_date}")
    print(f"Authorized: {'Yes' if is_authorized == 1 else 'No'}")

    today = datetime.now().date()
    expiry = datetime.strptime(expiry_date, "%Y-%m-%d").date()

    if is_authorized == 0:
        print("❌ Access Denied: This token is unauthorized.")
    elif today > expiry:
        print("⚠️ Access Denied: This token has expired.")
    else:
        print("✅ Access Granted: Token is valid.")
else:
    print("❌ Invalid Token ID.")

conn.close()