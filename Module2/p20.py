import random
import string

class User:
    def __init__(self, user_id, name, password):
        self.data = (user_id, name, password)

def generate_password(text):
    try:
        words = text.split()
        if len(words) == 0:
            raise ValueError("Enter some words")

        password = random.choice(words)

        password += random.choice(string.digits)
        password += random.choice("!@#$%")
        password += random.choice(string.ascii_uppercase)

        while len(password) < 8:
            password += random.choice(string.ascii_letters)

        return password

    except Exception as e:
        print("Error:", e)

# Example
name = input("Enter name: ")
text = input("Enter words: ")

pwd = generate_password(text)

user = User(1, name, pwd)

print("Generated Password:", pwd)
print("User Data:", user.data)