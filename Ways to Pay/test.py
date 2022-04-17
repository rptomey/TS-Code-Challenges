def test(x):
    if x < 0:
        return 0
    elif x == 0:
        return 1
    else:
        a = test(x-1)
        b = test(x-2)
        c = test(x-3)
        return a + b + c