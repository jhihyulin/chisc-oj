input1, input2 = input().split()

input1 = int(input1)
input2 = int(input2)

data_list = []

for i in range(input1, input2 + 1):
    data_list.append(i)

for i in data_list:
    print(i, end=' ')
