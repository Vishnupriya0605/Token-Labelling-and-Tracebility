import sqlite3


conn = sqlite3.connect("tokendata.db")
cursor = conn.cursor()


cursor.execute("SELECT * FROM tokens")
tokens = cursor.fetchall()


print("TOKEN DATA:")
print("-----------")
for token in tokens:
    print(f"Token ID: {token[0]}")
    print(f"Issue Date: {token[1]}")
    print(f"Expiry Date: {token[2]}")
    print(f"Authorized: {'Yes' if token[3] == 1 else 'No'}")
    print("-----------")

conn.close()