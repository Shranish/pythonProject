weight=int(input('Enter the weight in kg/lbs :'))
unit=input('(L)bs or (K)g:')
if unit.upper()=="K":
    pounds=weight/0.453592
    print(pounds,'lbs')
if unit.upper()=="L":
    kg=weight*0.453592
    print(kg,'kg')

