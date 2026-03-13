def run():
    print("Simple Interest Calculator")

    principal = float(input("Ana para: "))
    rate = float(input("Faiz orani (%): "))
    time = float(input("Sure (yil): "))

    interest = principal * rate * time / 100
    total = principal + interest

    print("Faiz:", interest)
    print("Toplam tutar:", total)