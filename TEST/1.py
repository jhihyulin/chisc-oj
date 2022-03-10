import time
import random

dic = {
    0: "data_1",
    1: "data_2",
    2: "data_3",
    3: "data_4",
    4: "data_5",
    5: "data_6",
    6: "data_7",
    7: "data_8"
}

for i in dic:
    print(dic[random.randint(0,7)])
    time.sleep(1)