def run():
    print("Compound Growth Calculator")

    principal = float(input("Baslangic sermayesi: "))
    rate = float(input("Buyume orani (%): "))
    periods = int(input("Donem sayisi: "))

    total = principal * (1 + rate / 100) ** periods

    print("Toplam sermaye:", total)