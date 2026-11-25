import re
email = input("Enter your email : ")
user_name = r"[a-zA-Z_0-9]+([.-][a-zA-Z0-9]+)*"
domain_name = r'@(gmail|outlook)'
extension = r'\.(in|com|gov|org)$'

validation = user_name + domain_name + extension
valid_email = re.fullmatch(validation,email)
if valid_email != None:
    print(f"congrats,{email} its a valid email Adress".title())
else:
    print(f"{email} invalid email")
