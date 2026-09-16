from sys import argv

script, filename = argv

print(f"Checking file: {filename}")

f = open(filename, 'r')
print(f.read())
f.close()
