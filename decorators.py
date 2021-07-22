def wrapper_fn(original_fn):
	def inner_fn():
		print ("Inner function ran")
		return original_fn()
	return inner_fn

@wrapper_fn
def display():
	print("Decorator example")

display()
