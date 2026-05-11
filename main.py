import random as rd

print("Welcome to the OTP Generator & Verification System!")

# Generate a 6-digit OTP
def generate_otp():
    otp = rd.randint(100000, 999999)
    return otp

# Verify the OTP entered by the user
def verify_otp(generated_otp):
    user_input = int(input("Please enter the OTP: "))
    if user_input == generated_otp:
        print("OTP verified successfully!")
    else:
        print("Invalid OTP. Please try again.")

# Main function to run the OTP generator and verification
def main():
    otp = generate_otp()
    print("An OTP has been generated.")
    print("Your OTP is: ", otp)  # In a real application, you would send this OTP to the user's email or phone number instead of printing it.

    user_choice = input("Do you want to verify the OTP? (yes/no): ")
    if user_choice == "yes":
        verify_otp(otp)
    
    else:
        print("Verification skipped.")

if __name__ == "__main__":    
    main()