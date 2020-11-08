dlist=[1,2,2,3,3,4,4,5,5];
s1=set(dlist);

print(s1);

print( 1 in s1);
print (10 in s1);

s1.add(7);
print(s1);
s1.add(7);
print(s1);
s1.remove(7);
print(s1);

set1={1,2,3};
set2={3,4,5};
print(set1);
print(set2);
print(set1.intersection(set2));

print(set1.difference(set2));
print(set2.difference(set1));
print(set1.union(set2));
print(set1);
set1.clear();
print(set1);


l1 = [1,2,3,4,5];
l2 = [5,6,7];
fs1 = frozenset(l1);
fs2 = frozenset(l2);

print(fs1);
print(fs2);

print(type(fs1));

print(fs1.intersection(fs2));

print(fs1.union(fs2));