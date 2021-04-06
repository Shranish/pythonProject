name=input('Enter your name:')
if len(name)<3:
    print('Name should be of atleast 3 charecters.')
elif len(name)>50:
    print('Maximum length of your name is 50 charecters')
else:
    print('Your name looks good.')