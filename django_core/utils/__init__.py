import random
import time

def generate_unique_code(length=12):
    timestamp_part = str(int(time.time() * 1000))[-6:]  # Lấy 6 số cuối từ timestamp
    random_digits = ''.join(random.choices('0123456789', k=length - 6))
    full_code = f"{timestamp_part}{random_digits}"
    return int(full_code)
