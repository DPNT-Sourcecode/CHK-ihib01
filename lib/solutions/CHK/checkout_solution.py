from typing import List

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if skus == '':
        return 0
    elif type(skus) != str:
        return -1
    else:
        separated = list(skus)
        
        hash_map = {
            "A": {"count": 0, "price": 50, "special_count": 0},
            "B": {"count": 0, "price": 30, "special_count": 0},
            "C": {"count": 0, "price": 20},
            "D": {"count": 0, "price": 15}   
        }
     
        hash_map["A"]["count"] = separated.count("A")
        hash_map["B"]["count"] = separated.count("B")
        hash_map["C"]["count"] = separated.count("C")
        hash_map["D"]["count"] = separated.count("D")

        if separated.count("A") % 3 == 0:
          hash_map["A"]["special_count"] = int(separated.count("A")/3)
          hash_map["A"]["count"] = 0
        elif separated.count("A") % 3 == 1 or separated.count("A") % 3 == 2:
          hash_map["A"]["count"] = separated.count("A") % 3
          hash_map["A"]["special_count"] = int((separated.count("A") - separated.count("A") % 3)/3)
        elif separated.count("B") % 2 == 0:
            hash_map["B"]["special_count"] = int(separated.count("B")/2)
            hash_map["B"]["count"] = 0
        elif separated.count("B") % 2 == 1:
            hash_map["B"]["count"] = separated.count("B") % 2
            
            
