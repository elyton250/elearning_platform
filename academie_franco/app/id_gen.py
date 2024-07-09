import random
import string

def generate_courseID():
    """
    Generates a unique 3-character ID consisting only of uppercase letters.
    """
    # Define the characters allowed in the ID (A-Z)
    allowed_chars = string.ascii_uppercase
    # Generate a random 3-character ID
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(3))
    return unique_id


def generate_userID():
    """
    Generates a unique ID of specified length.
    """
    allowed_chars = string.ascii_uppercase + string.digits
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(5))
    return unique_id



print(generate_userID())