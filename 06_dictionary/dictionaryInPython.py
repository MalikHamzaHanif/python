stdsInformation={
    "name":"hamza",
    "age":45,
    "phoneNumber":3175536782,
    "address":"nil"
}

print(stdsInformation)

print(stdsInformation["name"])
stdsInformation["address"]="new Address"
print(stdsInformation)

for key in stdsInformation:
    print(stdsInformation[key])

for key,value in stdsInformation.items():
    print(key,value)

newDict={x:x**4 for x in range(5)}
print(newDict)

print(newDict.get("name"))
print(newDict)
print(newDict.pop("name","hi"))
print(newDict)
print(newDict.popitem())
print(newDict)

for key in newDict:
    print(newDict[key])