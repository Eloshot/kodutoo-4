def double_hashing(data, max_value):
    # loome tühja rasi 
    hash_map = [None] * (max_value + max_value)
    new_max = len(hash_map)

    # teine hash funktsioon kus saame value 
    def second_hash(value):

        return 1 + round(value * 2)

    for item in data:
        index = item 

        while hash_map[index] is not None:
            # kui juhtub kokkuporge
            index = (index + second_hash(item)) % (new_max)

        hash_map[index] = item

    return hash_map

data = [4, 7, 1, 9, 2,11,2]
max_value = max(data)
result = double_hashing(data, max_value)

print(result)
