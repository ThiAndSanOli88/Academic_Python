def seqNum(f):
    a, b = 0, 1
    if f <= 0:
        return
    print(a)
    if f == 1:
        return
    print(b)
    for _ in range(2, f):
        c = a + b
        print(c)
        a, b = b, c
seqNum(30)