#lamdba test
a = lambda x,y: x*y

print(a(2,4))


#old way

def func(mylist):
    list_xy = []
    for x in range(10):
        for y in range(5):
            list_xy.append(x*y)
    return mylist+list_xy
    
    
print(func([1,2,3]))


lambda2 = lambda list:[x * y for x in range(10) for y in range(5)] + list

print("\nusing lambdas\n")
print(lambda2([1,2,3]))
        