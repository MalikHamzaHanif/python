# import time
# def timer(fn):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         result= fn(*args,**kwargs)
#         end=time.time()
#         print(f"function {fn.__name__} executed in {end-start} time")
#         return result
#     return wrapper

# # def activeSleep(n):
# #     time.sleep(n)

# # timer(activeSleep)(2)

# # def activeSleep(n):
# #     time.sleep(n)

# # newFn=timer(activeSleep)


# # newFn(2)

# # @timer
# # def activeSleep(n):
# #     time.sleep(n)
# # activeSleep=timer(activeSleep) this is what python do internally
# # activeSleep(2)



# # def debug(fn):
# #     def wrapper(*args,**kwargs):
# #         args_value=", ".join(str(arg) for arg in args)
# #         kwargs_value=", ".join(f"{k}={v}" for k,v in kwargs.items())
# #         print(f"{fn.__name__} is executed with args: {args_value} and kwargs: {kwargs_value}")
# #         fn(*args,**kwargs)
# #     return wrapper
# # @debug
# # def helloSir(valOne,valueTwo,name,age):
# #     print("hi")


# # helloSir(4,2,name="ali",age=34)


# def cacheFn(fn):
#     cache_value={}
#     def wrapper(*args):
#         print(cache_value)
#         if(args in cache_value):
#             return cache_value[args]
#         result=fn(*args)
#         cache_value[args]=result
#         return result
#     return wrapper

# import time
# @cacheFn
# def sum(a,b):
#     time.sleep(2)
#     return a+b

# print(sum(3,5))
# print(sum(3,5))
# print(sum(3,5))
# print(sum(3,4))

def noOfEachChar(userStr):
    convertToStr=str(userStr)
    frequencyOfEachChar={}
    for char in userStr:
        if(char==" "):
            continue
        if frequencyOfEachChar.get(char.lower())!=None:
            continue
        frequencyOfEachChar[char.lower()]=convertToStr.count(char.lower())
        print(char)
    return frequencyOfEachChar    

fr=noOfEachChar("Hello World")

print(fr)