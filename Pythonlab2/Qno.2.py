# WAP which accepts marks of four subjects and display total marks, percentage and grade.
a=int(input('Enter the marks of first subject='))
b=int(input('Enter the marks of second subject='))
c=int(input('Enter the marks of third subject='))
d=int(input('Enter the marks of fourth subject='))
total_marks=a+b+c+d
print('Your total marks=',total_marks)
percentage=((total_marks)/400)*100
print('Your percentage is',percentage)
if (percentage)>70:
    print('Your grade is distinction')
elif (percentage)>60:
    print('Your grade is first div')
elif (percentage)>40:
    print('Your grade is pass')
elif (percentage)<40:
    print('You failed')