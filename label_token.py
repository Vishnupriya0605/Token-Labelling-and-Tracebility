import sqlite3
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


token_id = input("Enter Token ID (e.g., github001): ")
qr_image_path = f"sample_qrs/{token_id}.png"


conn = sqlite3.connect("tokendata.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM tokens WHERE token_id = ?", (token_id,))
data = cursor.fetchone()

if data:
    issue_date, expiry_date, is_authorized = data[1], data[2], data[3]
    today = datetime.now().date()
    expiry = datetime.strptime(expiry_date, "%Y-%m-%d").date()

    
    if is_authorized == 0:
        label_text = "UNAUTHORIZED"
        label_color = (255, 0, 0)  # Red
    elif today > expiry:
        label_text = "EXPIRED"
        label_color = (255, 165, 0)  # Orange
    else:
        label_text = "VALID"
        label_color = (0, 128, 0)  # Green

    
    try:
        img = Image.open(qr_image_path).convert("RGBA").convert("RGB")
    except FileNotFoundError:
        print(f"❌ QR image not found: {qr_image_path}")
        conn.close()
        exit()

    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    
    draw.rectangle([(0, 0), (img.size[0], 25)], fill=(255, 255, 255))
    draw.text((10, 5), label_text, fill=label_color, font=font)

    
    labeled_path = f"sample_qrs/{token_id}_labeled.png"
    img.save(labeled_path)

    print(f"\n✅ QR image labeled and saved as: {labeled_path}")
else:
    print("❌ Token ID not found in database.")

conn.close()