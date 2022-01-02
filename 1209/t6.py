input_count = input()

input_count = int(input_count)

while input_count > 0:
    n,u,d = input().split()
    n = int(n)
    u = int(u)
    d = int(d)

    already_climbed = 0
    climb_time = 0

    while already_climbed < n:
        if already_climbed < n:
            already_climbed += u
            climb_time += 1
            if already_climbed >= n:
                break
        already_climbed -= d
        climb_time += 1
    input_count -= 1
    print(climb_time)