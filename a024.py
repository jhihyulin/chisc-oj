sex = input()
age = input()

sex = int(sex)
age = int(age)

if sex == 1:
    if age < 18:
        print('You are NOT marriageable.')
    else:
        print('You are marriageable.')
elif sex == 2:
    if age < 16:
        print('You are NOT marriageable.')
    else:
        print('You are marriageable.')