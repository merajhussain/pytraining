#datatype conversions

num =2;
fl = 2.0;
print(type(num));
print(type(fl));

print( type(str(num)));

s = '5';
print(s);
print(int(s));
print(type(int(s)));

t1=[1,2,3];
l1 = list(t1);

print(l1);
print(type(l1));
t2= tuple(l1);
print(t2);
print(type(t2));

num =10;
num_bin = bin(num);
print(num_bin);
num_hex= hex(num);
print(num_hex);

num_dec = int(num_bin,2);
print(num_dec);

num_dec = int(num_hex,16);
print(num_dec);
