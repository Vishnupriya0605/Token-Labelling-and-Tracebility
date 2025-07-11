import qrcode
import sqlite3
from datetime import datetime
import os


if not os.path.exists("sample_qrs"):
    os.makedirs("sample_qrs")


conn = sqlite3.connect('tokendata.db')
cursor = conn.cursor()


num_tokens = int(input("How many tokens do you want to generate? "))

for i in range(num_tokens):
    print(f"\n--- Enter details for Token {i+1} ---")
    token_id = input("Enter Token ID : ")
    issue_date = input("Enter Issue Date (YYYY-MM-DD): ")
    expiry_date = input("Enter Expiry Date (YYYY-MM-DD): ")
    label = input("Enter Label (e.g., GitHub Token): ")
    is_authorized = input("Is Authorized? (1 for Yes, 0 for No): ")

    
    cursor.execute("""
    INSERT OR REPLACE INTO tokens (token_id, issue_date, expiry_date, label, is_authorized)
    VALUES (?, ?, ?, ?, ?)
    """, (token_id, issue_date, expiry_date, label, int(is_authorized)))

    
    qr = qrcode.make(token_id)
    qr.save(f"sample_qrs/{token_id}.png")
    print(f"✅ QR generated and saved as {token_id}.png")


conn.commit()
conn.close()

print("\n🎉 All tokens added and QR codes generated successfully.")