def run():
    print("Currency Converter")

    amount = float(input("Para miktari: "))
    rate = float(input("Kur (exchange rate): "))

    result = amount * rate

    print("Sonuc:", result)
    