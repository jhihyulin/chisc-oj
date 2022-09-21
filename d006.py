data_num = int(input())

while True:
    if data_num == 0:
        break
    else:
        n,u,d = map(int, input().split())
        used_time = 0
        already_climbed = 0
        #n = n - 1
        while True:
            already_climbed = already_climbed + u
            used_time += 1
            if already_climbed >= n:
                break
            used_time += 1
            already_climbed = already_climbed - d
        print(used_time)
        data_num -= 1

