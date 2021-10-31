hh,mm = input().split()
hh = int(hh)
mm = int(mm)
if hh >= 17 or hh < 7:
    print ('Off School')
elif hh >=7 and hh < 17:
    if hh == 7 and mm < 30:
        print ('Off School')
    else:
        print ('At School')