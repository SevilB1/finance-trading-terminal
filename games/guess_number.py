import random

def play():
    print("Guess the Number")

    secret_number = random.randint(1, 10)

    guess = int(input("1 ile 10 arasinda bir sayi tahmin et: "))

    if guess == secret_number:
        print("Tebrikler! Dogru tahmin.")
    else:
        print("Yanlis tahmin.")
        print("Dogru sayi:", secret_number)