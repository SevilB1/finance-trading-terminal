while True:
    print("╔══════════════════════════════════╗")
    print("║     FINANCE & TRADING TERMINAL   ║")
    print("╠══════════════════════════════════╣")
    print("║      1 - Trading Tools           ║")
    print("║      2 - Investment Tools        ║")
    print("║      3 - Utilities               ║")
    print("║      4 - Games                   ║")
    print("║      5 - Exit                    ║")
    print("╚══════════════════════════════════╝")

    secim = input("Seciminiz: ")

    if secim == "1":
        import menus.trading_menu as tm
        tm.run()

    elif secim == "2":
        import menus.investment_menu as im
        im.run()

    elif secim == "3":
        import menus.utilities_menu as um
        um.run()

    elif secim == "4":
        import menus.games_menu as gm
        gm.run()

    elif secim == "5":
        print("Programdan cikiliyor...")
        break

    else:
        print("Gecersiz secim!")












