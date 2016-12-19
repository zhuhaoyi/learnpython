import math

for x in range(0, 3):
    def age(num):
        if num > 18:
            print('old')
        elif num < 18:
            print('young')
        else:
            print('i don\'t konw')

    text = input("type your age\nage:")
    text = int(text)
    age(text)

print('完毕')