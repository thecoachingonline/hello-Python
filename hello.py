import numpy as np
from lwe import KeyGenerator, Encryptor, Decryptor

# สร้างคีย์ลับ
key_generator = KeyGenerator(4096)
secret_key, public_key = key_generator.generate()

# เข้ารหัสข้อความ
message = "สวัสดีชาวโลก"
ciphertext = Encryptor(public_key).encrypt(message)

# ถอดรหัสข้อความ
plaintext = Decryptor(secret_key).decrypt(ciphertext)

print(plaintext)