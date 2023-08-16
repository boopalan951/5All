#Else
Name=input('What is your name : ')
if Name=='john snow':
    print('Hello john snow')
else:
    print(f'Hello {Name}')

#Complete Conditional Statement
if Name[0]=='A':
    print('Name Start with Letter A')
elif Name[1]=='A':
    print('Name Start with Letter B')
elif Name[2]=='A':
    print('Name Start with Letter C')
else:
    print('Name Start with Letter {}'.format(Name[0]))
