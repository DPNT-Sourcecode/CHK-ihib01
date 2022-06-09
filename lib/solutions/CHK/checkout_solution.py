from typing import List

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if skus == '':
        return 0
    elif type(skus) != str:
        return -1
    else:
        list_of_skus = skus.split('')
        num_of_A = list_of_skus.count("A")
        num_of_B = list_of_skus.count("B")
        num_of_C = list_of_skus.count("C")
        num_of_D = list_of_skus.count("D")
        total = 0
        if num_of_A % 3 == 0:
            special_price = num_of_A / 3 * 130
            total += special_price + num_of_B + num_of_C + num_of_D
        elif num_of_A % 3 == int:
            special_price = 130 * (num_of_A - (num_of_A % 3))/3
            total += special_price + (num_of_A % 3 * 50) + num_of_B + num_of_C + num_of_D
        elif num_of_B % 2 == 0:
            special_price = num_of_B / 2 * 45
            total += special_price + num_of_A + num_of_C + num_of_D
        elif num_of_B % 2 == int:
            special_price = 45 * (num_of_B - (num_of_B % 2))/2
            total += (special_price + (num_of_A % 3 * 30)) + num_of_A + num_of_C + num_of_D

        else:
            total += (num_of_A + num_of_B + num_of_C + num_of_D)
            
            
            
            
            



