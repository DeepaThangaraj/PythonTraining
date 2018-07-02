#program to find basic calculations
def add(x,y):
    return x+y
def division(x,y):
    return x/y
def multiplication(x,y):
    return x*y
def subtraction(x,y):
    return x-y

print('Select Operation:')
print('1.Addtion')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')

operation=input('Enter your option(1/2/3/4):')
number1=input('Enter the first number')
number2=input('Enter the second number')

if(operation==1):
    print(number1,"+",number2,"=",add(number1,number2))
elif(operation==2):
    print(number1,'-',number2,'=',subtration(number1,number2))
elif(operation==3):
    print(number1,'*',number2,'=',multiplication(number1,number2))
elif(operation==4):
    print(number1,'/',number2,'=',division(number1,number2))
else:
    print('Invalid input')

