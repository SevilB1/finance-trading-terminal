def run():
    print("Percentage Change Calculator")

    old_price = float(input("Eski deger: "))
    new_price = float(input("Yeni deger: "))

    change = ((new_price - old_price) / old_price) * 100

    print("Yuzde degisim:", change, "%")