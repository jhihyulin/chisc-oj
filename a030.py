try:
    while True:
        num = int(input())
        for i in range(2, num):
            if num % i == 0:
                print("No")
                break
        else:
            print("Yes")
except EOFError:
    pass