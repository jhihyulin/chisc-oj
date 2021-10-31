costumer_count = input()
trade_count = input()


while trade_count > 0:
    costumer_number,trade_type,amount = input().split()
    costumer_number = int(costumer_number)
    trade_type = int(trade_type)
    amount = int(amount)

    trade_count = trade_count - 1

#UNSOLVED