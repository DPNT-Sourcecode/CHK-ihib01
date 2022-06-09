

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if skus != str:
        return -1
    else:
        hash_map = {}
        for sku in skus:
            if sku not in hash_map:
                hash_map[sku] = 1
            else:
                hash_map[sku] += 1
                


