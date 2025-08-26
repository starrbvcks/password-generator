import random
import string

def make_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_1 = ""
    for i in range(length):
        password_1 += random.choice(characters)
    return password_1

length = int(input("enter legnth:"))
password = make_password(length)

print("your pass is:" , password)
