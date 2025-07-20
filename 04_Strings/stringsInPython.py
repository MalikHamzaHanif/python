str="i am hamza hanif"
print(str)
print(len(str))
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.startswith("i "))
print(str.endswith("i"))
print(str.split(" "))
print(str.find("hamza"))
print(str.count("hamza"))
print(str.index("hamza"))
print(str.replace("hamza","ali"))
print(str.replace("hamza","ali"))
print(str[:])
print(str[0:5])
print(str[5:10])
print(str.strip())

sentence="my name is {} and love to {} "
print(sentence.format("hamza","code"))

strOne="hi"
strTwo="hi"
print(strOne is strTwo)
print(strOne == strTwo)


for letter in str:
    print(letter)


myStr="i\nali"
print(myStr)
myRawStr=r"i\nali"
print(myRawStr)


subject=["chem","math","urdu"]

print(",".join(subject))