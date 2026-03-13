import random
import string

def play():

    print("Password Generator")

    length = int(input("Sifre uzunlugu kac olsun?: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Olusturulan sifre:", password)