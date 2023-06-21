# Lists: orderd, mutable, allows duplicate elements

"""
***Topics**
1- create list
2- for loop in list
3- if condetion in list
4- get length for list => len() method
5- append item in list => appand() method
6- remove item last item => pop() method
7- remove spcifc item => remove() method
8- clear all items form list => clear() method
9- reverse items in list => reverse() method
10- copy list => copy(), list(), etc 
11- create list with mutable items
12- to merge two lists 
13- start and stop index in list
14- comperhesion => fast way to create list with experssion and loop 
"""

# 1- create list 
my_list = ["A", "B", "C"]
my_list2 = [1, 2, 3, 4, 5, 7]

# 2- for loop in list
for x in my_list:
    print(x)

# 3- if condetion 
if "A" in my_list:
    print("yes")
else:
    print("no")

# 4- get length for list => len() method
a = len(my_list)
print(a)

# 5- append item in list => appand() method
my_list.append("w")
print(my_list)

# 6- remove item last item => pop() method
my_list.pop()
print(my_list)

# 7- remove spcifc item => remove() method
my_list.remove("B")
print(my_list)

# 8- clear all items form list => clear() method
my_list.clear()
print(my_list)

# 9- reverse items in list => reverse() method
my_list2.reverse()
print(my_list2)

# 10- copy list => copy(), list(), etc
list_copy = my_list2.copy()
# or
list_copy = list(my_list2)
# or 
list_copy = my_list2[:]
print(list_copy)


# 11- create list with mutable items
my_list3 = [2] * 5
print(my_list3)

# 12- to merge two lists 
w = my_list3 + my_list2
print(w)

# 13- start and stop index in list
b = my_list2[1:5]
print(b)
m = my_list2[:2]
print(m)
# step index
y = my_list2[::2]
print(y)

# 14- comperhesion => fast way to create list with experssion and loop 

number_list = [i*i for i in my_list2]
print(number_list)