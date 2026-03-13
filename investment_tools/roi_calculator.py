def run():
    print("ROI Calculator")

    investment = float(input("Yatirim miktari: "))
    final_value = float(input("Son deger: "))

    roi = ((final_value - investment) / investment) * 100

    print("ROI (%):", roi)