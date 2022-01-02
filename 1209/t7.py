input_count = input()

input_count = int(input_count)

while input_count > 0:
    input_1, input_2 = input().split()
    input_1 = int(input_1)
    input_2 = int(input_2)

    data_1 = bin(input_1)
    data_2 = bin(input_2)

    different_count = 0

    data_1 = list(data_1)
    data_2 = list(data_2)

    new_list = []
    for i in data_1:
        if i == 'b':
            i = 0
        i = int(i)
        new_list.append(i)
    data_1 = new_list

    new_list = []
    for i in data_2:
        if i == 'b':
            i = 0
        i = int(i)
        new_list.append(i)
    data_2 = new_list

    for i in data_1:
        if i != data_2[i]:
            different_count += 1

    print(different_count)

    input_count -= 1