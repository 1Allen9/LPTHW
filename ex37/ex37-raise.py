'''
def check_age(age):
	if age < 0:
		raise ValueError("Can't less than 0")
	return age

check_age(-1)
'''
def raise_test(n):
	try:
		print("num is",int(n))
	except ValueError:
		raise ValueError("n must be a number")

raise_test(666)
raise_test("a")
