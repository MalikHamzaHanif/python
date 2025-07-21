# # age=input("enter your age")
# age=45
# if(not age.isnumeric()):
#     print("age is non numeric")
# elif age.isnumeric():
#     ageInNumber=int(age)
#     if ageInNumber<13:
#         print("you can not access this code")
#     elif ageInNumber<20:
#         print("you are teenager")
#     elif ageInNumber<25:
#         print("you are adult")
#     else:
#         print("you are old ")
# else:
#     print("no case matched45")

# ticketPrice=12
# ticketPriceForChildren=8
# dicount=2

# userAge=int(input("enter your age \n"))
# day=input("enter day \n")
# str="your age is {} and today is {} so you will pay {}"
# if userAge>=18 and day=="wednesday":
#     print(str.format(userAge,day,ticketPrice-dicount))
# elif userAge<18 and day=="wednesday":
#     print(str.format(userAge,day,ticketPriceForChildren-dicount))
# elif userAge<18 and day!="wednesday":
#     print(str.format(userAge,day,ticketPriceForChildren))
# elif userAge>18 and day!="wednesday":
#     print(str.format(userAge,day,ticketPrice))

# day="wednesday"
# age=0
# price=12 if age>=18 else 8

# price-=2 if day=="wednesday" else price

# print(price)

day="wednesday"

match day:
    case "monday":
        print("you said monday")
    case "tuesday":
        print("you said tuesday")
    case _:
        print("you neighter said monday or tuesday")