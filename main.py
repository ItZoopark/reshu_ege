def f():
    x = 1
    while True:
        x += 1
        xc = x
        S = xc
        R = 0
        while xc > 0:
            d = xc % 2
            R = 10 * R + d
            xc = xc // 2
        S = R + S
        if len(str(S)) == 5:
            print(x)
            break


def f_35996(x):
    a = 3 * x + 23
    b = 3 * x - 17
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 20:
        return True
    else:
        return False


x = 5
while True:
    print(x)
    x += 1
    if f_35996(x):
        print(x)
        break



