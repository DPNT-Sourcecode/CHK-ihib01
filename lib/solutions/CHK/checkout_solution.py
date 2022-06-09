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
            if not sku.isalpha() or not sku.isupper():
                return -1
            else:
                hash_map[sku]["count"] += 1
        total = 0
        for key, value in hash_map.items():
            if key == "A" and value["count"] % 3 == 0:
                total += value["count"]/3 * 130
                next()
            elif key == "B" and value["count"] % 2 == 0:
                total += value["count"]/2 * 45
                next()
            total += value["count"] * value["price"]
        return total
            
            








