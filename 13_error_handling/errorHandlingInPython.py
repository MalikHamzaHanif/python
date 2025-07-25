try:
    myTextFile=open("file.txt","r")
    print(myTextFile.read())

finally:

    myTextFile.close()
    print("done")


with open("fileTwo.txt","w") as file:
    file.write("i am a file")

with open("fileTwo.txt","r") as file:
    print(file.read())

myTuple=("hamza","ali","shahid","hamza","ali","rehman")
print(myTuple)

myList=enumerate(myTuple)
myList=list(myList)

for key,value in myList:
    print(value)

myDict={"name":"ali","age":3}

for std in myDict:
    print(std)
for key,value in myDict.items():
    print(key,value)