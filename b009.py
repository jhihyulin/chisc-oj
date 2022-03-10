hh, mm = map(int, input().split())

if hh >= 17:
    print('Off School')
elif hh < 7:
    print('Off School')
elif hh == 7 and mm < 30:
    print('Off School')
else:
    print('At School')
