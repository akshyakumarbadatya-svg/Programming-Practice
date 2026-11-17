# # Notes--
# class NegativeAgeError(Exception):
#     pass
# class NotanageError(Exception):
#     pass
# #Step 2: Implementation
# def check_age(age):
#     if age < 0:
#  #Step 3: Raising
#         raise NegativeAgeError("Age cannot be negative")

#     elif age >= 200:
#         raise NotanageError("age should be less than 200 ")
# # Step 4: Handling
# try:
#     user_age = int(input("Enter age: "))
#     check_age(user_age)
# except NegativeAgeError as e:
#         print("Custom Exception:", e)
# except NotanageError as a:
#         print(a)
# else:
#         print("Valid Age: ",user_age)


'''this is my code'''
class NegativeAgeError(Exception):
    pass
class InvalidAgeError(Exception):
    pass
def check_age(age):
    if age < 0:
        raise NegativeAgeError("Age must be positive value only")
    elif age >= 200:
        raise InvalidAgeError("Age can't be morthan 200")
try:
    age = int(input("Enter Age : "))
    check_age(age)
except (ValueError,NegativeAgeError,InvalidAgeError) as Ex:
    print(Ex)
else:
    print("Else Part ")
finally:
    print("Finally completed")