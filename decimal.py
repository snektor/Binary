
while 1:

    a = input()
    b = 0

    for i in range(len(a)):
        if a[len(a)-1-i] == "1":
            b += 2**i

    print(b)
