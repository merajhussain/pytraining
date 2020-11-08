#dictionaries

d1 = {};
print(type(d1));

d1={"vendor":"lenovo","ram":"16gb","processor":"core i7"};
print(d1["vendor"]);

d1["vendor"]='hp';
print(d1);
print(len(d1));

print('lenovo' in d1); 

print(d1.keys());  

print(d1.values());  

print(d1.items()); 

tup = d1.items();

print(dir(type(tup)));