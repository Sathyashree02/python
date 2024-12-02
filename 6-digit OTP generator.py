import random

def generate_otp(length=6):
    digits = "0123456789"
    otp = "".join(random.choice(digits) for _ in range(length))
    return otp

# Generate a 6-digit OTP
otp = generate_otp()
print(f"Your OTP is: {otp}")
