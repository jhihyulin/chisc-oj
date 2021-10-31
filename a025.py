try:
    while True:
        s1,s2,s3 = input().split()
        s1 =int(s1)
        s2 =int(s2)
        s3 =int(s3)
        data_list = [s1,s2,s3]
        data_list.sort()
        if data_list[0] + data_list[1] > data_list[2]:
            print('Yes')
        else:
            print('No')
except EOFError:
    pass