def run():
    while True:
        print("╔══════════════════════════════════╗")
        print("║            UTILITIES             ║")
        print("╠══════════════════════════════════╣")
        print("║      1 - Percentage Change       ║")
        print("║      2 - Currency Converter      ║")
        print("║      3 - Tax Calculator          ║")
        print("║      4 - Back to Main Menu       ║")
        print("╚══════════════════════════════════╝")

        secim = input("Seciminiz: ")

        if secim == "1":
            import utilities.percentage_change as pc
            pc.run()

        elif secim == "2":
            import utilities.currency_converter as cc
            cc.run()

        elif secim == "3":
            import utilities.tax_calculator as tc
            tc.run()

        elif secim == "4":
            break

        else:
            print("Gecersiz secim!")