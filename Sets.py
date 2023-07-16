# Sets: unordered, mutable, no duplicates

""" 
***Topics***
1- Create Sets
2- union()
3- intersection()
4- difference()
5- symmetric_difference()
6- intersection_update()
7- difference_update()
8- symmetric_difference_update()
9- is_subset()
10- issuperset()
11- forzenset() 
"""
# 1- create Set 
a = set([1, 2, 3])
b = {1, 2, 3}

# 2- union: Will create a new set with all the elements from sets provided
s1 = {1, 2, 3}
s2 = {3, 4, 5}
res1 = s1.union(s2)
print(res1)

# 3 - intersection() or &: will return a set wit only the elements that are common to all of them
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s1.intersection(s2, s3) #return {3}

# 4- difference : difference or - will return only the elements that are unique to the first set (invoked set).
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s1.difference(s2)  # or 's1 - s2'
# {1}

s2.difference(s1) # or 's2 - s1'
# {4}

# 5-set symetric_difference: symetric_difference or ^ will return all the elements that are not common between them.
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.symmetric_difference(s2)  # or 's1 ^ s2'
# {1, 4}

