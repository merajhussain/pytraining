my_var=10;

def globVar():
	global my_var;
	print(my_var);
	my_var = 20;


globVar();
print(my_var);