my_tup=();
type(my_tup);
my_tup =(1);
print(type(my_tup));
my_tup=(1,);
print(type(my_tup));
my_tup =(1,2,3,4,5);
print(my_tup);
t1=("val1","val2","val3");

(v1,v2,v3) = t1;
print(v1);
print(v2);
print(v3);

a=[];
b=();
print(type(a));
print(type(b));

print(dir(a));
print("\n");
print(dir(b));

print(len(my_tup));

my_tup = ("a", "h", 32, 2.6, None, False);

print(my_tup[::-1]);