# ''' 1.When we don't know the exact exception name - normal way of handling the exception'''
# try:
#     n=int(input("Enter a Number :"))
#     print(f"Entered number is {n}".title())
# except:
#     pass# print("some error occured")
# else :
#     print("its optional but partially needed")
# finally:
#     print("Execution completed.")


# ''' 2.when we know the error name -handling the specific Exception'''

# try:
#     n=int(input("Enter a Number :")) #doubtful code
# except ValueError:
#     print("Please Enter Only integer")
# else: 
#     ("just an optional")
# finally:
#     print('Execution Done')

# ''' 3.when we know the error name and using alias name - prviding alias name for exception '''

# print("programme started ")
# try:
#     number1 = int(input("Eneter a num : "))
#     number2 = int(input("Eneter a num2 : "))
#     res = number1/number2
#     print("The division of two num is : ",res)

# except ValueError as ve:
#     print(ve)
# finally:
#     print("programme Execetion is successfully done ")

# ''' 4.Handling Multiple Exceptions using multiole except blocks ''' 

# l = [12,23,44,5,54,9]
# try:
#     i = int(input(("Enter a index Number :")))
#     res = l[i]
#     print(f"the value of the index positon {i} is {res}")
# except ValueError as ve:
#     print(ve)
# except IndexError as ie:
#     print(ie)
# else :
#     print("Executing....the last step") 
# finally:
#     print("Program done") 
    
# ''' 5. however we got an dis-advantage (every exception write line by line) of the above process so we need another process instead that we can use this process
# -----> handling Multilple Exceptions in a single line <--------
# '''

# try:
#     a = int(input("enter value of a : "))
#     b = int(input("enter value of b : "))
#     res = a/b
#     print(f"the division of both num {a},{b} is {res}")
# except (ValueError,ZeroDivisionError) as er:
#         print(er)
# else :
#     print("Eles block is optional but partially required")
# finally:
#     print("it executes at the end ")


# ''' 6.Handling Multiple Exceptions using exception class'''
# try:
#     a = int(input("enter value of a : "))
#     b = int(input("enter value of b : "))
#     res = a/b
#     print(f"the division of both num {a},{b} is {res}")
# except Exception as er:   #Exception class handle all the Errors
#         print(er)
# else :
#     print("its an optional block")
# finally:
#     print("it executes at the end ")

'''8. Using Nested try and except block:
A try-except block placed inside another try or except block to handle different
exceptions.'''

# details = {
#     "Name" : "Akshya Kumar Badatya",
#     "State" : "odisha",
#     "Mobile Number" : 2349305488,
#     "Gmail" : 'akshyakumarbadatya@outlook.com'

# }
# print("start Executing ......")
# try:
#     key = input("Type here (name,state,mobile number,gmail) : ")
#     # change_name = input("Enter your New name : ")
#     try:
#         res = details[key]
#         # res1 = details.update(Name = change_name)
#         # print(f'oLD NAME  : {res}')
#         # print(f"New Name : {details[key]}")
#         # print(details)
#     except KeyError as e:
#         print("Please type(name,state,mobile number,gmail) Capitalize letter  ",e)
#     else:
#         print("Nested else block")
# except :
#     print("outside Excepet Block")
# else:
#     print("Execution Complete")

''' 9.using Raise Keyword and Handling Error'''

try:
    age = int(input("Enter your Age : "))
    if age < 0:
       raise ValueError ("Age can't be negative",age)
    elif age >=200:
        raise ValueError("Age can't be morethan 200")

except ValueError as e:
        print(e)
except ValueError as a:
    print(a)
else:
    print("Valid age ",age)
finally:
    print("Program Executed")