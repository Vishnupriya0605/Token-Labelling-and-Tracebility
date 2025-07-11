import sqlite3


conn = sqlite3.connect('tokendata.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS tokens (
    token_id TEXT PRIMARY KEY,
    issue_date TEXT,
    expiry_date TEXT,
    label TEXT,
    is_authorized INTEGER
)
''')

print("✅ Database and table created.")
conn.commit()
conn.close()