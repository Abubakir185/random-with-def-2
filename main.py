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

def raqamni_top(start, stop, step):
    random_son = random.randint(start, stop)
    urinishlar_soni = 0
    
    while True:
        son = int(input(f"Son kiriting ({start} - {stop}, {step}ta urunishingiz bor) : "))
        urinishlar_soni += 1
        
        if urinishlar_soni == step:
            print("Yutqazdingiz!")
            return urinishlar_soni

        if son < random_son:
            print("Kiritilgan son kichik.")
        elif son > random_son:
            print("Kiritilgan son katta.")
        else:
            print("Yutdingiz!")
            return urinishlar_soni


taxminlar_soni = raqamni_top(1, 100, 5)
print(f"Taxminlar soni: {taxminlar_soni}")

        
