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

def generate_game(start, stop, limit):
    taxminiy_son = random.randint(start, stop)
    urinishlar_soni = 0

    while True:
        kiritinlgan_son = int(input(f"Son kriting ({start}-{stop}): "))
        urinishlar_soni += 1

        if kiritinlgan_son < taxminiy_son:
            print("Kichik son kiritildi.")
        elif kiritinlgan_son > taxminiy_son:
            print("Kiritilgan son katta.")
        else:
            print("Yutdingiz")
            break
    
    return urinishlar_soni <= limit 
    

print(generate_game(1, 50, 5))

        
