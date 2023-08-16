x,y,z=10,20,10
sports='cricket'
if x>y:
    print('True')
print("False")

#----->
a=int(input('1.What is 5+5?'))
if a==10:
    print('1.1That is Correct..!')
print("1.2You are Wrong.!")
#----->

#AND<OR<NOT
if x==10 and y<x:
    print('2.Both R True')
print('2.1U might B Mistaken')

if x==100 or y<x:
    print('3.Both R True')
print('31U might B Mistaken')

#membership operator "in"
if 'd' in sports:
    print("4.{} conatain letter b".format(sports))
print("4.1{} does not conatain letter b".format(sports))

#membership operator " not in"
if 'd' not in sports:
    print("{}5. does not conatain letter b".format(sports))

#Elif

if x==y:
    print("6.X same as Y")
elif x!=y:
    print('6.1X is not equal to Y')
    if x==z:
        print('6.2 x same as z')
elif x!=z:
    print('6.3False')
print('6.4True')
#furthely we cannot use elif here coz we used default else in the condition
