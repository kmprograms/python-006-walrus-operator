def walrus_operator():
    # ---------------------------------------- 1 --------------------------------------
    # przed wprowadzeniem walrus operator
    x = 10
    print(x)

    # po wprowadzeniu walrus operator - mozesz od razu przypisac i jednoczesnie wykorzystac
    # wartosc zmiennej
    print(y := 10)

    # zastosowanie walrus operator do pracy z petla while
    # potrzeba jednoczesnej inicjalizacji oraz aktualizacji zmiennej

    # ---------------------------------------- 2 --------------------------------------

    # przed wprowadzeniem walrus operator
    words = list()
    word = input('Enter new word:')
    while word != 'q':
        words.append(word)
        word = input('Enter new word:')
    print(words)

    # po wprowadzeniu walrus operator
    words2 = list()
    while (word2 := input('Enter new word:')) != 'q':
        words2.append(word2)
    print(words2)


if __name__ == '__main__':
    walrus_operator()
