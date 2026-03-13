while True:
    print("╔══════════════════════════════════╗")
    print("║              GAMES               ║")
    print("╠══════════════════════════════════╣")
    print("║      1 - Guess the Number        ║")
    print("║      2 - Dice Roll               ║")
    print("║      3 - Rock Paper Scissors     ║")
    print("║      4 - Password Generator      ║")
    print("║      5 - Name Picker             ║")
    print("║      6 - Back to Main Menu       ║")
    print("╚══════════════════════════════════╝")

    secim = input("Seciminiz: ")

    if secim == "1":
        import games.guess_number as gn
        gn.play()

    elif secim == "2":
        import games.dice_roll as gdr
        gdr.play()

    elif secim == "3":
        import games.rock_paper_scissors as rps
        rps.play()

    elif secim == "4":
        import games.password_generator as pg
        pg.play()

    elif secim == "5":
        import games.name_picker as np
        np.play()

    elif secim == "6":
        break

    else:
        print("Gecersiz secim!")
 