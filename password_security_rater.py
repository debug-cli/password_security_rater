import string

def check_password_strength(password):
    special_chars = "!@#$%^&*()_+-=[]{};:,.<>?/"
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in special_chars:
            has_special = True

    # Calculate the rating based on criteria met
    rating = 0
    if has_upper:
        rating += 1
    if has_lower:
        rating += 1
    if has_number:
        rating += 1
    if has_special:
        rating += 1

    # Determine strength based on rating
    if len(password) >= 8 and rating >= 3:
        strength = "Strong"
    elif len(password) >= 6 and rating >= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength

# Message before entering the password
print("Please enter your password. It will be checked for strength. No passwords are saved.")

# Input the password
user_password = input("Enter your password: ")

# Check password strength
password_strength = check_password_strength(user_password)

# Display result
print("________________________________       ________________________ ")
print(r"""\________________________________       ________________________ 
___  __ \__    |_  ___/_  ___/_ |     / /_  __ \__  __ \__  __ \
__  /_/ /_  /| |____ \_____ \__ | /| / /_  / / /_  /_/ /_  / / /
_  ____/_  ___ |___/ /____/ /__ |/ |/ / / /_/ /_  _, _/_  /_/ / 
/_/     /_/  |_/____/ /____/ ____/|__/  \____/ /_/ |_| /_____/  
                                                                
_______________________________________                         
___  __ \__    |__  __/__  ____/__  __ \                        
__  /_/ /_  /| |_  /  __  __/  __  /_/ /                        
_  _, _/_  ___ |  /   _  /___  _  _, _/                         
/_/ |_| /_/  |_/_/    /_____/  /_/ |_|                          
                                                                
                                                                
   _____________  __                                            
   ___  __ \_  / / /                                            
_____  /_/ /  /_/ /                                             
_(_)  .___/_\__, /                                              
   /_/     /____/                                               """)
print(f"The password is {password_strength}. No passwords are saved for your security.")

