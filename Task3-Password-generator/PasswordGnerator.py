import random
import string

def generate_password(length):
    """
    Generate a random password of the specified length."""
    
    if length < 4:
        print("Password length should be atleast 4 to include all character types.")
        return None
    
    #Define the character pools
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    #Ensure the password contains at least one character from each pool
    
    password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(digits),
        random.choice(special_chars)
        
    ]
    
    # Fill the remaining length with random choices from all character types
    all_characters = lower_case + upper_case + digits + special_chars
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the characters to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")
        
if __name__ == "__main__":
    main()
    