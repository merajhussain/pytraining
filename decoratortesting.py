#decorator test

def my_decorator(target_function):
	def function_wrapper():
		return "Testing decorator"+target_function()
	return function_wrapper()
    

@my_decorator
def target_function():
    return "coolest"
    
  
print(str(target_function()))