t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0

while count < 9:
    while True:
        if count == 9:
            break

        x = int(input("x = ")) - 1
        if t[x] == 'x' or t[x] == 'o':
            continue
        t[x] = 'x'
        count += 1
        print(f"{t[0]} | {t[1]} | {t[2]}", f"{t[3]} | {t[4]} | {t[5]}", f"{t[6]} | {t[7]} | {t[8]}",
              sep='\n---------\n')
        print('\n')
        break

    if t[0] == t[1] == t[2] == "x" or t[3] == t[4] == t[5] == "x" or t[6] == t[7] == t[8] == "x" or \
            t[0] == t[3] == t[6] == "x" or t[1] == t[4] == t[7] == "x" or t[2] == t[5] == t[8] == "x" or \
            t[0] == t[4] == t[8] == "x" or t[2] == t[4] == t[6] == "x":
        print("x yutdi!!!")
        break

    while True:
        if count == 9:
            break

        y = int(input("o = ")) - 1
        if t[y] == 'o' or t[y] == 'x':
            continue
        t[y] = 'o'
        count += 1
        print(f"{t[0]} | {t[1]} | {t[2]}", f"{t[3]} | {t[4]} | {t[5]}", f"{t[6]} | {t[7]} | {t[8]}",
              sep='\n---------\n')
        print('\n')
        break

    if t[0] == t[1] == t[2] == "o" or t[3] == t[4] == t[5] == "o" or t[6] == t[7] == t[8] == "o" or \
            t[0] == t[3] == t[6] == "o" or t[1] == t[4] == t[7] == "o" or t[2] == t[5] == t[8] == "o" or \
            t[0] == t[4] == t[8] == "o" or t[2] == t[4] == t[6] == "o":
        print("o yutdi!!!")
        break
else:
    print("Durrang!!!")
