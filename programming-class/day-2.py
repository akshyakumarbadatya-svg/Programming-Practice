'''# 1.
# row = int(input("Enter How many rows you want : "))
# column = int(input("Enter How many columns you want : "))

# value = 1
# for i in range(row):
#     for j in range(column):
#         print(value,end=" ")
#         value +=1
#     print()
#     value += 1
#     if value > 9:
#         value = 1'''



''' 2.
# row = int(input("Enter How many rows you want : "))
# column = int(input("Enter How many columns you want : "))

# # value = 1
# for i in range(row):
#     value = 1
#     for j in range(column):
#         print(value,end=" ")
#         value +=1
#     print()
#     value += 1
#     if value > 9:
#         value = 1'''


'''3.
row = int(input("Enter How many rows you want : "))
column = int(input("Enter How many columns you want : "))
value = 1
for i in range(row):
    for j in range(column):
        print(value,end=" ")
        value +=1
        if value > 9:value = 1
    print()
    value += 1
    if value > 9:
        value = 1'''

'''4.
row = int(input("Enter How many rows you want : "))
column = int(input("Enter How many columns you want : "))
value = 9
for i in range(row):
    for j in range(column):
        print(value,end=" ")
        value -=1
        if value < 1:value = 9
    print() '''
    
    
'''5.    
row = int(input("Enter How many rows you want : "))
column = int(input("Enter How many columns you want : "))
value = row
if value > 9:
    value=9
for i in range(row):
    for j in range(column):
        print(value,end=" ")
        # if value < 1:value = 9
    print()
    value -=1
    if value < 1: value=9 '''
#  6.

row = int(input("Enter How many rows you want : "))
column = int(input("Enter How many columns you want : "))
for i in range(row):
    value = column
    for j in range(column):
        print(value,end=" ")
        value -=1
    print()
    

        
    