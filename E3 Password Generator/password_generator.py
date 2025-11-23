import random
import string

def generate_password(length, use_upper, use_numbers, use_symbols):
    """
    Generates a random password based on the specified criteria.

    Args:
        length (int): The length of the password.
        use_upper (bool): Whether to include uppercase letters.
        use_numbers (bool): Whether to include numbers.
        use_symbols (bool): Whether to include symbols.

    Returns:
        str: The generated password.
    """
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_yes_no_input(prompt):
    """
    Prompts the user for a yes/no answer.

    Args:
        prompt (str): The prompt to display.

    Returns:
        bool: True if the user enters 'y' or 'yes', False otherwise.
    """
    while True:
        response = input(prompt).lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

def main():
    print("--- Password Generator ---")
    
    while True:
        try:
            length_input = input("Enter the desired password length: ")
            length = int(length_input)
            if length <= 0:
                print("Length must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    use_upper = get_yes_no_input("Include uppercase letters? (y/n): ")
    use_numbers = get_yes_no_input("Include numbers? (y/n): ")
    use_symbols = get_yes_no_input("Include symbols? (y/n): ")

    password = generate_password(length, use_upper, use_numbers, use_symbols)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
