def myfunc():
    "Help string for myfunc()";
    print("hello func");
	
myfunc();

x = [1,2,3,4,5];
def myfunc(x):
    "myfunc with param"
    print(x);
    
myfunc(x);


x= [1,2,3,4,5];
y = [6,7,8,9];

def my_func(x,y):
    "myfunc with 2 params"
    x.extend(y);
    print(x);
    
my_func(x,y);


def my_func(x):
    "myfunc with return"
    return x*x;
    
print("sqaure of 2 is :"+str(my_func(2)));


def funcWithArgs(x,*args):
    print(x);
    print(args);
    for ar in args:
        print(ar);
    
    
funcWithArgs(10,1,2,3);