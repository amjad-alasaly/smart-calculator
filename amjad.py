 
num1 = float(input('Inter The First Number:    '))
operation = input(' Inter The Operation:        ')
num2 = float(input('Inter The scenod Number:    '))

if operation == '+' :
    print (num1 + num2)
elif operation == '*':
    print (num1 * num2) 
elif operation == '-' :
    print (num1 -num2)
elif operation == '%' :
    print (num1 % num2)
elif  operation == '/' :
    if num2 == 0 :
        print('Eroor')
    else:
        print ( num1 / num2)
   

   

