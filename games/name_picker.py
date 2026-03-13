import random

def play():
    print("Name Picker")

    names = input("Virgul ile isimleri giriniz: ")

    name_list = names.split(",")

    selected_name = random.choice(name_list)

    print("Secilen isim:", selected_name)