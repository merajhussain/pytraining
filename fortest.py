x = range(0,10);

for a in x:
	print(a);
    

my_string = 'python';

for letter in my_string:
    print(letter*2);

print("\n------------- testing indexes---------------\n");   
vendors = ['hp','intel','cisco','dell'];

print(vendors);
for vendor in vendors:
    print(vendor + " at index: "+str(vendors.index(vendor)));
   