def win_or_loss(a, b):
    if (a==0&b==2)|(a==2&b==5)|(a==5&b==0):
        return "Win"
    elif a == b:
        return "Draw"
    else:
        return "Loss"


F_out = int(input())
N_out = int(input())
sister_out_list = map(input().split(), int)

broth_out_list = [F_out]
brother_out = F_out
game_list = []
already_round = 0

for i in sister_out_list:
    game_out = win_or_loss(brother_out, i)
    if game_out == "Win":
        game_win_o_lose = 'Win'
        continue
    elif game_out == 'Loss':
        game_win_o_lose = 'Loss'
        continue


    game_list.append(game_out)
    if i[0] ==broth_out_list[i-2]:
        brother_out = 

game_win_o_lose = ##

print(broth_out_list,game_win_o_lose,'at round', already_round)