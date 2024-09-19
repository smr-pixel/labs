
#First Task
def make_set(nums_list):
    new_list = []
    for num in nums_list:
        if num not in new_list:
            new_list = new_list + [num]
    return new_list

#list_to_set = make_set([1, 2, 3, 4, 4, 5])
#print(list_to_set)

#Second Task
def is_set(given_list):
    if given_list != None:
        new_list = make_set(given_list)
        if new_list == given_list:
            set_bool = True
        else:
            set_bool = False
    else:
        set_bool = False
    return set_bool

#set_or_not = is_set([4, 3])
#print(set_or_not)

#Third Task
def union(set_a, set_b):
    if is_set(set_a) == True and is_set(set_b) == True:
        set_a_b = set_a + set_b
        set_a_b = make_set(set_a_b)
    else:
        set_a_b = []

    return set_a_b

#full_set = union([1, 1, 1], [2, 3])
#print(full_set)

#Fourth Task
def intersection(set_a, set_b):
    if is_set(set_a) == True and is_set(set_b) == True:
        set_ab = [value for value in set_a if value in set_b]
    else:
        set_ab = []

    return set_ab

#inter_set = intersection([1, 1, 1], [2])
#print(inter_set)
