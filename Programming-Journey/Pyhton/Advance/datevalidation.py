import re 
date = input("Enter the date (DD-MON-YYYY or DD.MM.YYYY)")

Date = r'(0[1-9]|1[0-9]|2[0-9]|3[0-1])'
# first_space = r'\-'
# Month = r'(0[1-9]|1[0-2])'
month_name = r'(jan|feb|mar|apr|may|june|jul|aug|sep|nov|oct|dec)'.upper() 
# second_space =r'\-'
Year = r'\d{4}'
valid_date = (
    Date + r'\.' + month_name + r'\.' + Year +
    r'|' +
    Date + r'\-' + month_name + r'\-' + Year
)
check_valid_date = re.fullmatch(valid_date,date) 
print(check_valid_date)

if check_valid_date != None:
    print("Valid date")
else : 
    print("invalid date")