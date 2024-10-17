import re

def phoneNumber(phone):
    pattern = r'^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

def social(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern,ssn))

def zipCode(zip):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern,zip))

def prompt_for_valid_input(prompt_message, validation_function):
    while True:
        user_input = input(prompt_message)
        if validation_function(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def main ():
    phone = prompt_for_valid_input("Please enter your phone number(Format: 555-555-5555 or (555) 555-5555): ",phoneNumber)
    print("Phone number is valid")
    ssn = prompt_for_valid_input("Please enter your SSN(Format: 555-55-5555): ", social)
    print("SSN is valid")
    zip = prompt_for_valid_input("Please enter your zip code(Format: 55555 or 55555-5555): ",zipCode)
    print("Zip code is valid")

main()    