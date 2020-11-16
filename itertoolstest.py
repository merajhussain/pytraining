from itertools import *
list1 = [1,2,3,'a','b','c']

list2 = [101,102,103,'X','Y']

chain(list1,list2)

for i in chain(list1,list2):
	print(i)

    
 

print(list(filterfalse(lambda x: x <5,[1,2,3,4,5,6,7,8,9])))


x = list(range(10))

print( x[2:9:2])

print(list(islice(range(10),2,9,2)))


	