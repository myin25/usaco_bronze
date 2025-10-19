'''with open("gymnastics.in.py") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

print(content)

# create matrix
for i in range(len(content)):
    content[i] = content[i].split(" ")
print(content)




# take input from the file by creating a list
myfile = open("gymnastics.in.py","r")
temp = myfile.read().split(" ")
check("myFile without edits " + str(temp))
myfile.close() # we have to also remember to close the file after initially opening it

# removing the unecessary sections
fileinput = temp[::2]
print("edited input " + str(fileinput))
'''





# open file input
myfile = open("gymnastics.in.py","r")

content = myfile.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
    content[i] = content[i].split(" ")
print(content)

# create master list
fileinput = [int(content[0][0]), int(content[0][1])]
for row in range(int(content[0][0])):
    for col in range(int(content[0][1])):
        fileinput.append(int(content[row + 1][col]))

print(fileinput)
