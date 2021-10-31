input()
score_list = input().split()

score_list = list(map(int, score_list))

print(max(score_list),min(score_list))