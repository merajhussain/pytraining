#nesting

l1 = [1,2,3,8,200];
l2 = [4,5,6,18,200];

for i in l1:
    for j in l2:
        if i * j < 100:
            print(i*j);
        elif i*j > 200:
            pstr = str(i*j);
            print(pstr+" is greater than 200, hence breaking");
            break;
        else:
            pstr = str(i*j);
            print(pstr+" is > 100 so it is not printed");
               
			
       