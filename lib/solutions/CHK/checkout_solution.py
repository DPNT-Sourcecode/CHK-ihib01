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
            "A": {"count": 0, "price": 50, "special_count": 0},
            "B": {"count": 0, "price": 30, "special_count": 0},
            "C": {"count": 0, "price": 20},
            "D": {"count": 0, "price": 15}   
        }
        for sku in skus:
            if not sku.isalpha() or not sku.isupper():
                return -1
            else:
                if hash_map[sku] == "A" and hash_map[sku]["count"] == 3:
                    hash_map[sku]["special_count"] += 1 and hash_map[sku]["count"] = 0
                elif hash_map[sku] == "B" and hash_map[sku]["count"] == 2:
                    hash_map[sku]["special_count"] += 1 and hash_map[sku]["count"] = 0
                hash_map[sku]["count"] += 1
        total = 0
        for key, value in hash_map.items():
            
            total += value["count"] * value["price"]
        return total
            
            




