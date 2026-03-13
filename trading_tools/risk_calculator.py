def run():
    print("Risk Calculator")

    balance = float(input("Hesap bakiyesi: "))
    risk_percent = float(input("Risk yuzdesi (%): "))

    risk_amount = balance * risk_percent / 100

    print("Riske edilecek tutar:", risk_amount)