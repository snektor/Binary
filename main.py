
while 1:

    a = int(input())
    b = []
    c = ""

    while 1:

        if a == 1:
            b.append(1)
            break

        b.append(a - (a // 2) * 2)
        a = a // 2

    b.reverse()
    for i in range(len(b)):
        c = str(c + str(b[i]))

    print(c)
