try:
    while True:
        name = input()
        print('hello,',name)
except EOFError:
    pass