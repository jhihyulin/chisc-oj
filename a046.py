try:
    while True:
        input_data = int(input())
        if input_data >= 35:
            print("建國高中")
        elif input_data >= 28:
            print("大安高工資訊科")
        elif input_data >= 27:
            print("大直高中")
        elif input_data >= 26:
            print("內湖高中")
        elif input_data >= 23:
            print("中和高中")
        elif input_data >= 21:
            print("新店高中")
        elif input_data >= 19:
            print("華江高中")
except EOFError:
    pass