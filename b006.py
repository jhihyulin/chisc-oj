try:
    while True:
        a, b = map(int, input().split())
        # if a < b:
        #     c = a
        #     a = b
        #     b = c
        if a%b == 0:
            print('Yes')
        else:
            print('No')
except EOFError:
    pass