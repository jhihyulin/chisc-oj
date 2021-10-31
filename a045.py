try:
    while True:
        in_count,back_count = input().split()
        in_count = int(in_count)
        back_count = int(back_count)
        in_list = range(1,in_count + 1)
        back_list = input().split()
        back_list = list(map(int, back_list))
        if in_count != back_count:
            different_list = list(set(in_list).symmetric_difference(set(back_list)))
            for i in different_list:
                print(i,end=' ')
            print()
        else:
            print('*')
except EOFError:
    pass