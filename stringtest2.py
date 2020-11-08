x ="cisco";
y = "switch";
print(x+y);
print(x*3);

print("O" in x);
print("o" in x);

format  = "Integer %d, float %f, string %s";

print(format%(1,1.2,"string format"));

formatusingfunction = "Integer {}, float {}, string {}";
print(formatusingfunction.format(1,1.2,"string format"));