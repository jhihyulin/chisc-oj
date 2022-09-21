while True:
    try:
        f = int(input())
        n = int(input())
        y = input()
        y = list(map(int, y.split()))
        pre = -1
        g = 0
        for i in range(n):
            h = y[i]
            print(f, end=' ')
            # 程式贏
            if( (f == 0 and h == 2) or (f == 2 and h == 5) or (f == 5 and h == 0) ):
                print(': Won at round', i + 1)
                g = 1
                break
            # 程式輸
            elif( (f == 5 and h == 2) or (f == 0 and h == 5) or (f == 2 and h == 0) ):
                print(': Lost at round', i + 1)
                g = -1
                break
            if pre == h:
                if h == 0:
                    f = 5
                elif h == 2:
                    f = 0
                elif h == 5:
                    f = 2
            pre = h
        if g == 0:
            print(': Drew at round', n)
    except EOFError:
        break