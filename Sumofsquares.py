#Program to find sum of squares upto x


x = int(input("Enter the limit :"))
sum = 0
for i in range(1,x+1):
    sum = sum + i*i
print(f"Sum of squares of all numbers upto {x} = {sum} ") 
