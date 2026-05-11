# Python_OTP_Generator
# OTP Generator
A lightweight, secure, and easy-to-use One-Time Password (OTP) generator.

## ✨ Features
- Generate random OTPs (4 to 10 digits)
- Support for TOTP (Time-based OTP)
- Support for HOTP (Counter-based OTP)
- Cryptographically secure random generation
- Customizable length and expiry time
- CLI support for quick use
- Simple and clean API

## 📦 Installation

pip install otp-generator

**Or clone the repository:**

git clone https://github.com/yourusername/OTP_Generator.git
cd OTP_Generator
pip install -r requirements.txt

## 🚀 Usage

### Basic OTP Generation

from otp_generator import generate_otp

# Generate 6-digit OTP
otp = generate_otp(length=6)
print(f"Your OTP: {otp}")

### TOTP (Recommended for 2FA)

from otp_generator import TOTP

totp = TOTP(secret="your_base32_secret_here")

# Get current OTP
current_otp = totp.now()
print(f"Current TOTP: {current_otp}")

# Verify OTP
is_valid = totp.verify("123456")
print(f"Is valid: {is_valid}")

### Command Line Usage

# Generate 6-digit random OTP
python -m otp_generator --length 6

# Generate TOTP
python -m otp_generator --totp --secret "JBSWY3DPEHPK3PXP"

# Show all options
python -m otp_generator --help

## 🛠 Configuration

| Option       | Default | Description                       |
|--------------|---------|-----------------------------------|
| `length`     | 6       | OTP length (4-10)                 |
| `expiry`     | 30      | Expiry time in seconds (TOTP)     |
| `algorithm`  | SHA1    | Hash algorithm (SHA1, SHA256)     |

## 📁 Project Structure

OTP_Generator/
├── src/otp_generator/
│   ├── __init__.py
│   ├── generator.py
│   ├── totp.py
│   └── utils.py
├── tests/
├── examples/
├── requirements.txt
├── setup.py
└── README.md

## 🧪 Running Tests

pytest tests/

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/yourusername/OTP_Generator/issues).

## 📄 License

This project is licensed under the **MIT License**.

**Made with ❤️**

Give this project a ⭐ if you found it useful!

Just copy everything above and save it as `README.md` in your project folder.

Would you like me to adjust anything (add badges, change tone, add screenshots section, etc.)?
