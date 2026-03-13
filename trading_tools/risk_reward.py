def run():
    print("Risk / Reward Calculator")

    entry = float(input("Giris fiyati: "))
    stop_loss = float(input("Stop loss: "))
    take_profit = float(input("Take profit: "))

    risk = abs(entry - stop_loss)
    reward = abs(take_profit - entry)

    ratio = reward / risk

    print("Risk:", risk)
    print("Reward:", reward)
    print("Risk / Reward Orani:", ratio)