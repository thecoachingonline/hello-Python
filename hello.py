import hashlib

# แปลงข้อความเป็น bytes
message = b"Hello World!"

# แฮชข้อความ
hashed_message = hashlib.sha256(message).hexdigest()

# พิมพ์ค่าแฮช
print(hashed_message)