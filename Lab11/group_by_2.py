def group_by(f, target_list: list):
    result = {}
    for item in target_list:
        key = f(item)
        if key in result:
            result[key].append(item)
        else:
            result[key] = []
    return result

length = group_by(len, ['hi', 'dog', 'me', 'bad', 'good'])
print(length)