

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if skus != str:
        return -1
    else:
        hash_map = {
            "A": {"count": 0, "price": 50},
            "B": {"count": 0, "price": 30},
            "C": {"count": 0, "price": 20},
            "D": {"count": 0, "price": 15}   
        }
        for sku in skus:
            hash_map[sku] += 1
        total = 0
        for key in hash_map.keys():
            total += key["count"] * key["price"]
        return total
            
            



