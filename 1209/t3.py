input1,input2,input3 = input().split()

input1 = int(input1)
input2 = int(input2)
input3 = int(input3)

data_1 = input1*input2

if(data_1 > input3):
    print('Greater')
elif(data_1 == input3):
    print('Equal')
elif(data_1 < input3):
    print('Less')