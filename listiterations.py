#list comprehensions


#using for loop
list1=[];

for i in range(10):
    result = i **2;
    list1.append(result);
    
    
print(list1);


#using comprehenstions
list2 = [x ** 2 for x in range(10)];
print(list2);

list3 = [ x ** 2 for x in range(10) if x > 5]
print(list3)

#for sets
set1 = {  x ** 2 for x in range(10)};
print(set1)

#for dictionaries

dict1 = {x : x*2 for x in range(10)}

print(dict1)
    