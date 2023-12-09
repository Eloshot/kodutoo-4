def hashing(data, max_value):
    # Initsialiseeri tühi massiiv
    hash_map = [None] * (max_value + 1)
    
    for item in data:
        # Kasuta andmete väärtusi indeksitena ja salvesta need massiivi
        hash_map[item] = item 
    
    return hash_map

data = [4, 7, 1, 9, 2]
max_value = max(data) # kasutame maks väärtust listi suurusena
result = hashing(data, max_value)

print(result)
