stds=["hamza","ali","shahid","hadi","asim","shameer","hammad"]

print(stds)

print(stds[2])
print(stds.pop())
stds.append("new Student hamza hanif")
print(stds)
stds.insert(1,"malik mohiz awan new student")
print(stds)
stds.remove("hamza")
print(stds)
print("hamza" in stds)

if "ali" in stds:
    print("ali is present inside the students")

for std in stds:
    print(std)

listTwo=[x**2 for x in range(5)]
print(listTwo)

listthree=listTwo.copy()

print(listthree)