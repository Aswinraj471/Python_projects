#Program to find the multiplication table


num = int(input("Enter the number : "))

for i in range(1,11):
    print(f'{num} X {i} = {num*(i)}')
    print("\r")
