def run():
    while True:
        print("====================================")
        print("         TRADING TOOLS")
        print("====================================")
        print("1 - Risk Calculator")
        print("2 - Position Size")
        print("3 - Profit / Loss")
        print("4 - Risk / Reward")
        print("5 - Break Even")
        print("6 - Back to Main Menu")
        print("====================================")

        secim = input("Seciminiz: ")

        if secim == "1":
            import trading_tools.risk_calculator as rc
            rc.run()

        elif secim == "2":
            import trading_tools.position_size as ps
            ps.run()

        elif secim == "3":
            import trading_tools.profit_loss as pl
            pl.run()

        elif secim == "4":
            import trading_tools.risk_reward as rr
            rr.run()

        elif secim == "5":
            import trading_tools.break_even as be
            be.run()

        elif secim == "6":
            break

        else:
            print("Gecersiz secim!")