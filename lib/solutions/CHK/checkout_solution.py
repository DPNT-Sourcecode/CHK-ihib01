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
        for i in separated:
            if not i.isalpha() or not i.isupper():
                return -1
        
        hash_map = {
            "A": {"count": 0, "price": 50, "special_count": 0, "special_price": 130},
            "B": {"count": 0, "price": 30, "special_count": 0, "special_price": 45},
            "C": {"count": 0, "price": 20, "special_count": 0, "special_price": 0},
            "D": {"count": 0, "price": 15, "special_count": 0, "special_price": 0},
            "E": {"count": 0, "price": 40, "special_count": 0, "special_price": 0}   
        }
     
        hash_map["A"]["count"] = separated.count("A")
        hash_map["B"]["count"] = separated.count("B")
        hash_map["C"]["count"] = separated.count("C")
        hash_map["D"]["count"] = separated.count("D")
        hash_map["E"]["count"] = separated.count("E")
        total = 0
        if separated.count("A") % 5 == 0:
            hash_map["A"]["special_count"] = int(separated.count("A")/5)
            hash_map["A"]["special_price"] = 200
            hash_map["A"]["count"] = 0
        elif separated.count("A") % 5 == 3:
            hash_map["A"]["special_count"] = int((separated.count("A")-3)/5)
            hash_map["A"]["special_price"] = 200
            hash_map["A"]["count"] = 0
            total += 130
        elif separated.count("A") % 5 == 1 or separated.count("A") % 5 == 2:
            hash_map["A"]["special_count"] = int((separated.count("A") - separated.count("A") % 5)/5)
            hash_map["A"]["special_price"] = 200
            hash_map["A"]["count"] = separated.count("A") % 5
        elif separated.count("A") % 5 == 4:
            hash_map["A"]["special_count"] = int((separated.count("A")-4)/5)
            hash_map["A"]["special_price"] = 200
            hash_map["A"]["count"] = 1
            total += 130
        if separated.count("B") % 2 == 0:
            hash_map["B"]["special_count"] = int(separated.count("B")/2)
            hash_map["B"]["count"] = 0
        elif separated.count("B") % 2 == 1:
            hash_map["B"]["count"] = separated.count("B") % 2
            hash_map["B"]["special_count"] = int((separated.count("B") - separated.count("B") % 2)/2)     
        if separated.count("E") % 2 == 0 and separated.count("B") >= 1:
            hash_map["E"]["special_count"] = int(separated.count("E")/2)
            hash_map["E"]["special_price"] = -30
        for key, value in hash_map.items():
            total += (value["count"] * value["price"]) + (value["special_count"] * value["special_price"])
            
        return total
            
            
            







