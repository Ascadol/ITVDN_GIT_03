def inp_a():
    a = int(input("a: "))
    return(a)


def inp_b():
    b = int(input("a: "))
    return(b)


def dod():
    a = inp_a()
    b = inp_b()
    print(a + b)
    main()


def vid():
    a = inp_a()
    b = inp_b()
    print(a - b)
    main()


def main ():
    print("1. Додавання. 2. Віднімання. 3. Вихід")
    way = int(input("Оберіть шлях: "))


    if way == 1:
        dod()
    elif way == 2:
        vid()
    elif way == 3:
        return
    else:
        print("Введіть з наведених варіантів.")
        main()


if __name__ == "__main__":
    main()