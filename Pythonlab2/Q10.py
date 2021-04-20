num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))
num3=int(input('Enter the third number:'))
if num1==(num2 or num3):
    output=0
elif num2==(num1 or num3):
    output=0
elif num3==(num1 or num2):
    output=0
else:
    output=num1+num2+num3
print(output)