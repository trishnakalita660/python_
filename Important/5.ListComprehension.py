from typing import List


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = [ ]

for x in nums:
    new_list.append(x)

print('new_list is {}'.format(new_list))

# list comprehension

list_compre = [ n for n in nums]

print('list using comprehension {}'.format( list_compre))

# filter + lambda

f_list = [ n for  n in nums if n%2==0]
print(f_list)

filtered = filter(lambda n: n%2==0, nums)
filtered = list(filtered)
print (filtered)

#  Dictionary Comprehension

my_dict = [ (letter, num) for letter in 'abcd' for num in range(4)]

print(my_dict)

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G' ]
lowers= ['a', 'b', 'c', 'd', 'e', 'f', 'g']

joined_names = {}

for name, lower in zip(names, lowers):
    joined_names[name] = lower
print(joined_names)

dict_compre = {name:lower for name, lower in zip(names,lowers) if name!='A'}

print(dict_compre)

# Set

nums2 = [1,1,2,3,3,5,4,6,6,7,7,8,9,20,2,3,4,5]

myset = {n for n in nums}
print(myset)

# GENERATORS

mygen = (n *n for n in range(10))

for i in mygen:
    print(i)

