n,m = input().split()
n = int(n)
m = int(m)

score_list = []

while n > 0:
    input_score = int(input())
    score_list.append(input_score)
    n = n - 1

number_list = []

while m > 0:
    input_number = int(input())
    number_list.append(input_number)
    m = m - 1

for i in number_list:
    print(score_list[i - 1])