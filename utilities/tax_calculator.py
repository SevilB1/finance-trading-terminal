def run():
    print("Tax Calculator")

    amount = float(input("Tutar: "))
    tax_rate = float(input("Vergi orani (%): "))

    tax = amount * tax_rate / 100
    total = amount + tax

    print("Vergi tutari:", tax)
    print("Toplam tutar:", total)