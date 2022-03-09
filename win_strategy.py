def f_27803():
    x = 67

    f_1 = lambda x: x * 5
    f_2 = lambda x: x + 4
    f_3 = lambda x: x + 1
    f_1_rev = lambda x: x // 5
    f_2_rev = lambda x: x - 4
    f_3_rev = lambda x: x - 1

    a = [0] * (x + 1)
    # for i in range(x + 1): a[i] = 0

    win = min(f_1_rev(x), f_2_rev(x), f_3_rev(x)) + 1
    for i in range(win, x + 1): a[i] = 1
    n = win - 1
    while n != 0:
        if a[f_1(n)] < 0 or a[f_2(n)] < 0 or a[f_3(n)] < 0:
            neg_el = list(filter(lambda x: x < 0, [a[f_1(n)], a[f_2(n)], a[f_3(n)]]))
            a[n] = abs(max(neg_el)) + 1
        else:
            a[n] = -1 * max(a[f_1(n)], a[f_2(n)], a[f_3(n)])
        n -= 1

    print(a)

    for index, value in enumerate(a):
        if value == 2:
            print(index)


def f_27803_mansur(x, *commands):
    array = [0] * (x + 1)
    m = '+0'
    for command in commands:
        if command[0] == '*' and int(command[1]) > int(m[1]):
            m = command
    t = x // int(m[1]) + 1
    if x % int(m[1]) != 0:
        t += 1
    tc = t - 1
    while t != x + 1:
        array[t] = 1
        t += 1
    while tc != 0:
        minim = 1000
        prior = True
        for command in commands:
            tcc = tc
            tcc = eval('tcc' + command)
            if abs(array[tcc]) < abs(minim) and array[tcc] > 0 and prior:
                minim = -array[tcc]
            elif abs(array[tcc]) < abs(minim) and array[tcc] < 0:
                minim = -array[tcc] + 1
                prior = False
        array[tc] = minim
        tc -= 1
    i = 0
    while array[i] != -1:
        i += 1
    print(i)
    l = []
    for i in range(x + 1):
        if array[i] == 2:
            l.append(i)
    print(l)
    return array


def f_27803_anton():
    # s = [0] * int(input('от скольбки камбнмей выибграл: '))
    # actions = [input('введитбе операбцеюб: ') for _ in range(int(input('скольбко операбцийб: ')))]

    s = [0] * 68
    actions = ['+1', '+4', '*5']

    s[-1] = 1
    for i in range(len(s) - 1, -1, -1):
        nexts = []
        for action in actions:
            if action[0] == '+':
                next = i + int(action[1:])
            elif action[0] == '*':
                next = i * int(action[1:])

            if next < len(s):
                nexts.append(s[next])
            else:
                nexts.append(666)

        if min(nexts) < 0:
            s[i] = abs(min(nexts)) + 1
        elif 666 in nexts:
            s[i] = 1
        else:
            s[i] = -max(nexts)

    print('S:', *[i for i in range(1, len(s) + 1)], sep='\t')
    print('ходов:', *s, sep='\t')
    for i, x in enumerate(s):
        if x == -2:
            print(i)


# f_27803_anton()


def f_ege(edge, turn):
    a = [0] * (edge + 1)
    # +1, *2
    # threshold = edge // 2 + 1
    # a[threshold:] = [1]*(len(a) - threshold)
    for i in range(len(a)):
        if 5 * i > edge:
            a[i] = 1

    start = edge // 5
    for i in range(start, 0, -1):
        if a[i + 1] > 0 and a[i + 4] > 0 and a[5 * i] > 0:
            a[i] = max(a[i + 1], a[5 * i], a[i + 4]) * (-1)
        else:
            neg = list(filter(lambda x: x < 0, [a[i + 1], a[5 * i], a[i + 4]]))
            a[i] = abs(max(neg)) + 1
    print(a)
    for s in range(len(a)):
        if a[s] == turn:
            print(s)


# f_ege(67, 2)


def f_4109():
    edge = 49
    a = [0] * (edge + 1)
    for i in range(50 // 2, 70 // 2):
        a[i] = 1

    a[edge] = 1
    for i in range(edge - 1, 70 // 2 - 1, -1):
        if a[i + 1] > 0:
            a[i] = -a[i + 1]
        else:
            a[i] = -a[i + 1] + 1

    for i in range(50 // 2 - 1, 0, -1):
        if a[i + 1] > 0 and a[2 * i] > 0:
            a[i] = (-1) * max(a[i + 1], a[2 * i])
        else:
            neg = list(filter(lambda x: x < 0, [a[i + 1], a[2 * i]]))
            a[i] = abs(max(neg)) + 1
    for i in range(len(a)):
        if a[i] == -1:
            print(i)


# f_4109()
# Две кучи

def resh_ege_27416(turn):
    n = 2 * (69 + 1)
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if 2 * i + j >= 77 or 2 * j + i >= 77:
                a[i][j] = 1

    for _ in range(100):
        for i in range(n):
            for j in range(n):
                if a[i][j] == 0:
                    if a[i + 1][j] > 0 and a[i][j + 1] > 0 and a[2 * i][j] > 0 and a[i][2 * j] > 0:
                        a[i][j] = -max(a[i + 1][j], a[i][j + 1], a[2 * i][j], a[i][2 * j])
                    elif a[i + 1][j] < 0 or a[i][j + 1] < 0 or a[2 * i][j] < 0 or a[i][2 * j] < 0:
                        neg = list(filter(lambda x: x < 0, [a[i + 1][j], a[i][j + 1], a[2 * i][j], a[i][2 * j]]))
                        a[i][j] = abs(max(neg)) + 1

    CRED = '\33[43m'
    CEND = '\033[0m'
    for i in range(n):
        for j in range(n):
            if a[i][j] == -1:
                print(CRED + str(a[i][j]) + CEND, end='\t')
            else:
                print(a[i][j], end='\t')
        print()

    # for i in range(n):
    #     if a[7][i] == turn:
    #         print(i)


resh_ege_27416(-2)
