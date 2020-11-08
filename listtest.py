lists1 =[];
print(type(lists1));
lists1=["1","2","3",4,5.0,6];
print(lists1);

#lists are mutable
lists1[0]="one";
print(lists1);

mlist =[1,2,4];

print(min(mlist));

mlist.append(100);
print(mlist);

del mlist[2];
print(mlist);
mlist.append(4);
print(mlist);
mlist.pop();
print(mlist);
mlist.append(200);
print(mlist);
mlist.remove(200);
print(mlist);

list1=[1,2,3,4];
list2=[5,6,7,8];
list1.extend(list2);
print(list1);
list1.append(5);
print(list1);
print(list1.count(5));
print(list1);
list1.sort();
print(list1);

list1.append(25);
list1.append(22);
print(list1);
print(sorted(list1));
print(list1);


