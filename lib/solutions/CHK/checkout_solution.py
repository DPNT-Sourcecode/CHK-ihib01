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
            
            

