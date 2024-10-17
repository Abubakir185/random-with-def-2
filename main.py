# 1

import random


for i in range(1, 11):
    print(random.randint(1, 100))




#  2


import random

random_son = random.randint(1, 50)
urinishlar_soni = 0
    
son = int(input("Taxminiy son kiriting: "))


if son < random_son:
    print("Kiritilgan son kichik.")
elif son > random_son:
    print("Kiritilgan son katta.")
elif son == random_son:
    print("Yutingiz!")

if son != random_son:
    urinishlar_soni += 1
    

while son != random_son:
        
    if son != random_son:
        urinishlar_soni += 1

    son = int(input("Yana urinib koring: "))
    
    if son < random_son:
        print("Kiritilgan son kichik.")
    elif son > random_son:
        print("Kiritilgan son katta.")
    elif son == random_son:
        print("Yutingiz!")

    
    if urinishlar_soni == 5:
        print("Urinishlar soni 5taga yetdi!")
        break
        