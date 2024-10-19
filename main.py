# 1

import random

random_numbers = []

def generate_rand_mum(start, stop):
    return random.randint(start, stop)



for i in range(1, 10):
    num = generate_rand_mum(1, 100)
    random_numbers.append(num)

print(random_numbers)




#  2


import random

random_son = random.randint(1, 50)
urinishlar_soni = 0
    
while son != random_son:
    son = int(input("son kiriting: "))
     urinishlar_soni += 1

    if son < random_son:
        print("Kiritilgan son kichik.")
    elif son > random_son:
        print("Kiritilgan son katta.")
    elif son == random_son:
        print("Yutingiz!")

    
    if urinishlar_soni == 5:
        print("Urinishlar soni 5taga yetdi!")
        break
        
