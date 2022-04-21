def count_letter(word, letter):
    "Bu funksiya wordni ichida nechta letter bor ekanligni returni qiladi."
    k = 0
    for i in word:
        if i == letter:
            k += 1
    return k
