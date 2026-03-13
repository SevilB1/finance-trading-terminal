def run():
    print("Position Size Calculator")

    balance = float(input("Hesap bakiyesi: "))
    risk_percent = float(input("Risk yuzdesi (%): "))
    stop_loss = float(input("Stop loss mesafesi: "))

    risk_amount = balance * risk_percent / 100
    position_size = risk_amount / stop_loss

    print("Riske edilecek tutar:", risk_amount)
    print("Pozisyon boyutu:", position_size)