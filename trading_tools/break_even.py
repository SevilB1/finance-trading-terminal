def run():
    print("Break Even Calculator")

    entry_price = float(input("Giris fiyati: "))
    loss_percent = float(input("Zarar yuzdesi (%): "))

    loss_amount = entry_price * loss_percent / 100
    new_price = entry_price - loss_amount

    recovery_percent = (loss_amount / new_price) * 100

    print("Zarar sonrasi fiyat:", new_price)
    print("Basabas icin gereken kazanc (%):", recovery_percent)