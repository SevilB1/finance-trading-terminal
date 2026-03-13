def run():
    print("Profit / Loss Calculator")

    entry_price = float(input("Giris fiyati: "))
    exit_price = float(input("Cikis fiyati: "))
    quantity = float(input("Miktar: "))

    result = (exit_price - entry_price) * quantity

    print("Kar / Zarar:", result)