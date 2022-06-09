from typing import List

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if skus == '':
        return 0
    elif type(skus) != str:
        return -1
    else:
        hash_map = {
            "A": {"count": 0, "price": 50},
            "B": {"count": 0, "price": 30},
            "C": {"count": 0, "price": 20},
            "D": {"count": 0, "price": 15}   
        }
        for sku in skus:
            if not sku.isalpha():
                return -1
            hash_map[sku] += 1
        total = 0
        for key in hash_map.keys():
            if key == "A" and key["count"] % 3 == 0:
                total += key["count"]/3 * 130
            elif key == "B" and key["count"] % 2 == 0:
                total += key["count"]/2 * 45
            total += key["count"] * key["price"]
        return total
            
            

