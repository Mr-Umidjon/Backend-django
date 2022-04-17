mehmonlar = {
    "Umidbek": ['19', 'standart'],
    "Odiljon": ['17', 'standart']
}


def show():
    print(f"Ismi    Xonasi  Xona Turi")
    for k, v in mehmonlar.items():
        print(
            f"{k}     {v[0]}  {v[1]}"
        )
    print('\n\n')


def plus():
    ism = input("Ism: ")

    def check():
        xona = input("Xona raqamini kiriting: ")
        for k, v in mehmonlar.items():
            if xona == v[0]:
                print("Bu xona band, boshqa xona tanlang:\n")
                return check()
        return xona

    xona = check()
    xona_turi = input("Xona turini quyidagi belgilar orqali tanlang:\n"
                      "\te - ekanom"
                      "\ts - standart"
                      "\tl - lyuks")
    if xona_turi == 'e':
        xona_turi = 'ekanom '
    elif xona_turi == 's':
        xona_turi = 'standart '
    if xona_turi == 'l':
        xona_turi = 'lyuks '
    mehmonlar[ism] = [xona, xona_turi]
    print(f'{ism.title()} mehmonlar ro\'yxatiga qo\'shildi.\n')


def minus():
    ism = input("Ism: ")
    if ism not in mehmonlar:
        print(f"{ism} ismli mehomon yo'q.\n"
              f"Iltimos ismni bosqattan kiriting:\n")
        return minus()
    mehmonlar.pop(ism)
    print(f"{ism} mehmonlar ro'yxatidan o'chirildi.\n")


def main():
    option = input("Mehmonxonamizga xush kelibsiz!!!\n"
                   "Buyruqni tanlang:\n"
                   "1 - Mehmon qo'shish\n"
                   "2 - Mehmonni ro'yxatdan chiqarish\n"
                   "3 - Mehmonlar ro'yxati\n\n"
                   "0 - Dasturdan chiqish\n")
    if option == '1':
        plus()
    elif option == "2":
        pass
        # minus()
    elif option == '3':
        show()
    elif option == '0':
        return 0
    return main()


main()
