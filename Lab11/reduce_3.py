from functools import reduce

def filter(function, strings):
    return reduce(lambda acc, item: acc + [item] if function(item) else acc, strings, [])

print(filter(lambda x: x != '', ['Happy', 'Holidays', '', 'Everyone']))

