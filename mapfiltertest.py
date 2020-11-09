#map filter usage
def p(x):
	return x*10
    
 
    

r = range(1,5)

print(list(map(p,r)));

#using lambdas

print(list(map(lambda x: x*10,r)))

print(list(filter(lambda x: x<3,r)))



