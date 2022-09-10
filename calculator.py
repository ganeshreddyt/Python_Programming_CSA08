#Calculator .....
def cal(symb):
    switch={
     '+':
        print('Addition is :',a+b),
     '-':
        print('Subtraction is:',a-b),
    '*':
        print('Multiplication is:',a*b),
     '/':
        print('Divison is:',a/b),
    '%':
        print('Modulus is:',a%b),
    }
    #return switch.get(symb,'Invalid operator')

a = int(input('Enter firstNum :'))
b = int(input('Enter secondNum :'))
symb = input('Enter symbol :')
cal(symb)
