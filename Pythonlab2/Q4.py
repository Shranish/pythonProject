a=int(input('Enter first integer:'))
b=int(input('Enter second integer:'))
c=int(input('Enter third integer:'))
if a<b and a<c:
    print('The smallest number is',a)
elif b<c and b<a:
    print('The smallest number is',b)
elif c<b and c<a:
    print('The smallest number is',c)
