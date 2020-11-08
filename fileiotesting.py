myfile = open("C:\\py\\laptops.txt","r");

print(myfile.mode);
myfile.seek(0);
print(myfile.read(5));


myfile.seek(0);
print(myfile.readlines());
myfile.seek(0);

for line in myfile.readlines():
    if line.startswith('a'):
        print(line);