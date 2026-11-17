# Date - 17th NOV 2026                   --poornima maam             class timings - 2:45/2:30-4:10

'''Approach 1: Explicitly creating a object for custom exception class'''

# class WeakPasswordError(Exception):
#     def __init__(self,password,message):
#         self.password = password
#         self.message = message
#     def check_pw(self):
#         if len(self.password) != 8 and len(self.password) !=> :
#             raise obj
# user_pw = input("Enter The Password ")
# length = len(user_pw)

# # creating object
# obj = WeakPasswordError(user_pw,"Password Should Be exactly 8 char")

# # handling Exception
# try:
#     obj.check_pw()
# except WeakPasswordError as e:
#     print(e)
# else:
#     print("Strong Password !😊")


'''Approach 2: without Explicit Object --- Recommanded Way of Handle Exception'''

class WeakPasswordError(Exception):
    def __init__(self,password):
        self.password = password
    def __str__(self):
        return f"WeakPassword : {self.password} Should have 8 char {len(self.password)}"
try:
    user_pw = input("Enter Your password : ")
    if len(user_pw) != 8 :
        raise WeakPasswordError(user_pw)
except WeakPasswordError as obj:
        print(obj)
else:
    print("strong Password")




# the Python and Oracle SQL assessment has been set for tomorrow at 2:00 PM For new FDE batch. However we have SQL,Javascript Webtech also

    