# my_set   = {1,2,3,4,5,5,6,6,5}

# my_set.add(8)

# my_set.remove(3)
# my_set.update([11,15,13])
# print(my_set.discard(133))
# copyt_set = my_set.copy()
# print(my_set.clear())
# print(my_set)
# print(copyt_set)


set_1 = {1,2,3,4,5}
set_2 = {6,4,7,8,2}

# it will return a unique set like . it will retun a set from two set only the unique values from those set

# union_set = set_1 | set_2
# print(union_set)


# it will return a unique set like . it will retun a set from two set only the  values from those set who are similar
# interSection_set = set_1 & set_2
# print(interSection_set)

# #it will return a set on where only first set value will be returned . it won't retun any values from the second set
# difference_set = set_1 - set_2
# print(difference_set)

# it will Returns a new set with elements in either set but not in both.
# symmetric_diff_set = set_1 ^ set_2
# print(symmetric_diff_set)

# if every value of a is avialible in b or more than but it should every value of a . if this condition is true then it's a subset . a could be smaller but it can't be larger than b.
# is_subset = set_1 <= set_2 . 
# print(is_subset)

# if every value of a is avialible in b or more than but it should every value of a . if this condition is true then it's a superset . a could be smaller but it can't be larger than b.
# is_subset = set_2 >= set_1 . 
# print(is_subset)


# if every element of both sets are unique then it's true and it will return a unique set or else it will return false
are_disjoint = set_1.isdisjoint(set_2)
print(are_disjoint)
