from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first varialbe is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
string = input("Get something ")
print(f"input get: {string}")
print("input GET: %s" %( string))
num1 = input("cal num1 = ")
num2 = input("cal num2 = ")
print("num1+num2=%d" %(int(num1)+int(num2)))
