def run():
    while True:
        print("====================================")
        print("        INVESTMENT TOOLS")
        print("====================================")
        print("1 - Compound Growth Calculator")
        print("2 - ROI Calculator")
        print("3 - Simple Interest Calculator")
        print("4 - Savings Goal Calculator")
        print("5 - Back to Main Menu")
        print("====================================")

        secim = input("Seciminiz: ")

        if secim == "1":
            import investment_tools.compound_growth as cg
            cg.run()

        elif secim == "2":
            import investment_tools.roi_calculator as roi
            roi.run()

        elif secim == "3":
            import investment_tools.simple_interest as si
            si.run()

        elif secim == "4":
            import investment_tools.savings_goal as sg
            sg.run()

        elif secim == "5":
            break

        else:
            print("Gecersiz secim!")