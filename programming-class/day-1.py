''' 1.swawpping of 3 num '''

'''# step 1 :-input the numbers'''
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number : "))
num3 = int(input("Enter the 3rd number : "))
# step-2 - before swap
# print(f'Before swapping\nnumber1: {num1}\tnumber2: {num2}\tnumber3: {num3}')

# step- 3- for swap variable or value

'''# logic:1
num4 = num1
num1 = num3
num3 = num2
num2 = num4'''

'''# logic:2 -using bitwise XOR operator
num1 = num1^num2^num3
num2 = num1^num2^num3
num3 = num1^num2^num3
num1 = num1^num2^num3 '''

'''# logic:3- using addition and floordivision
num1 = num1*num2*num3
num2 = num1//(num2*num3)
num3 = num1//(num2*num3)
num1 = num1//(num2*num3)'''

'''# logic:4-using unpacking opearator
num1,num2,num3 = num3,num3,num1'''

'''# logic:5 - using +,-'''

num1 = num1 + num2 + num3
num2 = num1 - (num2 + num3)
num3 = num1 - (num2 + num3)
num1 = num1 - (num2 + num3)

# step-4 : - after swap Displaying the value 

print(f"After swap\nnum1: {num1}\tnum2: {num2}\tnum3: {num3}")

''' 2. even or odd'''

number = int(input("Enter a num :"))
     
# 1. number % 2 ==0:'even'
# 2. number % 2 != 0:'odd'
# 3. number % 2 != 1:'even'
# 4. number % 2 == 1:'odd'
# 5. number % 2>0: 'odd'
# 6. (number //2)*2 == number :'even'
# 7. (number //2)*2 == number-1 'odd'
# 8. number & 1 == 0 'even'
# 9. number & 1 ==1:'odd'
# 10. number | 1 == number +1:  #'even'
# 11. number | 1 == number: #'odd'

if number & 1 ==1:
    print(f"Number {number} is odd")
else:
    print(f"Number {number} is Even")
    
      
    
 