from sys import argv #import argv feature

script, filename = argv  # define argv variable

txt = open(filename)     # open file of file name

print(f"Here's your file {filename}:")  # print filename got from argv 
print(txt.read())     			# print filename context

txt.close()
# print("Type the filename again:")
# file_again = input("> ")  		# use input to get a file's name

# txt_again = open(file_again)		# open file

# print(txt_again.read()) 		# print file context
# txt_again.close()
