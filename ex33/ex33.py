i = 0
numbers = []
'''
while i < 6:
	print(f"At the top i is {i}")
	numbers.append(i)

	i = i + 1
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
	print(num)
'''
def while_loop(cnt):
	start = 0
	while start < cnt:
		print(f"top	is {start}")
		numbers.append(start)
		start += 1
		print("Numbers now: ", numbers)
		print(f"bottom is {numbers[-1]}")

# while_loop(8)
# print("---- end, numbers is:", numbers)

def step_while_loop(cnt, step):
	start = 0
	while start < cnt:
		print(f"top	is {start}")
		numbers.append(start)
		start += step
		print("Numbers now: ", numbers)
		print(f"bottom is {numbers[-1]}")
# step_while_loop(8, 2)
# print("---- end, numbers is:", numbers)

for n in range(0,8):
	print(f"top is {n}")
	numbers.append(n)
	print("Numbers = ", numbers)
	print(f"bottom is ", numbers[-1])
print("---END, numbers = ", numbers)
