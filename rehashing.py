def double_hashing(data, max_value):
    # loome tühja rasi 
    hash_map = [None] * (max_value + max_value)
    new_max = len(hash_map)

    # teine hash funktsioon kus saame value 
    def second_hash(value):
        return 1 + round(value * 2)

    def rehash():
        nonlocal hash_map, new_max
        new_max = 2 * new_max
        new_hash_map = [None] * new_max

        # suurendame räsitabelit ja siis annab iga elemendile uue koha
        for item in hash_map:
            if item is not None:
                index = item
                while new_hash_map[index] is not None:
                    index = (index + second_hash(item)) % (new_max)
                new_hash_map[index] = item

        hash_map = new_hash_map

    for item in data:
        index = item

        while hash_map[index] is not None:
            # kui juhtub kokkuporge
            index = (index + second_hash(item)) % (new_max)

        hash_map[index] = item

        # vaatame räsitabeli koormustegurit
        load_factor = sum(1 for x in hash_map if x is not None) / new_max
        if load_factor > 0.75:
            rehash()
 
    return hash_map

data = [4, 7, 1, 9, 2, 2, 11, 7,]
max_value = max(data)
result = double_hashing(data, max_value)

print(result)