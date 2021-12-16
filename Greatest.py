#Program to find greatest number among 3 numbers

a = int(input('Enter number1 :'))
b = int(input('Enter number2 :'))
c = int(input('Enter number3 :'))

if a > b:
    if c > a :
        print(f'{c} Greater than {a},{b}')
    else:
        print(f'{a} Greater than {c},{b}')
else:
    if c > b:
        print(f'{c} Greater than {b},{a}')
    else:
        print(f'{b} Greater than {c},{a}')
