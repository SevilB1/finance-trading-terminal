def run():
    print("Savings Goal Calculator")

    goal = float(input("Hedef miktar: "))
    monthly_saving = float(input("Aylik birikim: "))

    months = goal / monthly_saving

    print("Hedefe ulasmak icin gereken ay sayisi:", months)