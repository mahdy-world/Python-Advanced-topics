# orderd, immutabl, allows deplicaute elements

"""
***Topics***
1- create tuple
2- access tuple items
3- get length of tuple
4- get index of element on tuple
5- to convert tuple to list
6- to convert list to tuple
7- start and end on tuple
8- add value to items on tuple
9- Tuple vs list
"""

# 1- create tuple
my_tuple = "Ahmed", 25, "cairo"
# or make it itrable
my_tuple2 = tuple(["ahmed", 25, "cairo"])
# or 
my_tuple3 = ("AHmed", 25, "cairo")
my_tuple4 = (1, 2, 3, 4, 5, 6)


# 2- access tuple items
a = my_tuple[1]
print(a)

# 3- get length of tuple
b= len(my_tuple)
print(b)

# 4- get index of element on tuple
c = my_tuple.index("Ahmed")
print(c)

# 5- to convert tuple to list
my_list = list(my_tuple)
print(my_list)

# 6- to convert list to tuple
my_new_tuple = tuple(my_list)
print(my_new_tuple)

# 7- start and end on tuple
n = my_tuple4[1:3]
print(n)

# 8- add value to items on tuple
person_tuple = "ahmed", 20, "aga"
name, age, city = person_tuple
print(name)
print(age)
print(city)

# 9- Tuple vs list
# get bytes 
import sys
list1 = [0,1,2, "ahmed", True]
tuple2 = (0,1,2, "ahmed", True)
print(sys.getsizeof(list1), "bytes")
print(sys.getsizeof(tuple2), "bytes")

# get time
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3)", number=1000000))