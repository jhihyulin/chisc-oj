count = input()
count = int(count)

tall_list = []

while count !=0:
    tall = input()
    tall_list.append(tall)
    count = count - 1

tall_list.reverse()
for i in tall_list:
    print(i)
