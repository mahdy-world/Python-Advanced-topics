# Key - value pairs, unordered, mutable

""" 
***Topics***
1- Create Dic
2- Access items
3- Remove item 
4- For loop in dic 
5- Get key & value from dic
6- Get copy from dic without effict in original one 
"""


#1- Create dic
# first way
my_dic = {"name": "ahmed", "age": 25, "city": "aga"}
# seconde way
my_dic2 = dict(name="ahmed", age=25, city="aga")

# 2- Access items
dic_item = my_dic["name"]
print(dic_item)

# 3- Remove item 
my_dic2.pop("name")
print(my_dic2)

# 4- For loop in dic
# 5- Get key & value from dic
for x, y in my_dic.items():
    print(x, y)
    
# 6- Get copy from dic without effict in original one
copy1 = dict(my_dic)
print(copy1) 
    
copy2 = my_dic.copy()
print(copy2)