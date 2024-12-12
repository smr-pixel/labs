def zipmap(key_list, value_list, override = False):
    if not override and len(key_list) != len(set(key_list)):
        return None
    
    result = map(lambda x, y: (x, y), key_list, value_list + [None] * (len(key_list) - len(value_list)))
    return dict(result)

list_1 = ['a', 'b', 'c', 'd', 'e', 'f']
list_2 = [1, 2, 3, 4, 5, 6]

list_3 = [1, 2, 3, 2]
list_4 = [4, 5, 6, 7]

list_5 = [1, 2, 3]
list_6 = [4, 5, 6, 7, 8]

list_7 = [1, 3, 5, 7]
list_8 = [2, 4, 6]


print(zipmap(list_1, list_2))
print(zipmap(list_3, list_4, True))
print(zipmap(list_5, list_6))
print(zipmap(list_7, list_8))
