#2. Write a Python Program to Find Factorial of Number Using Recursion?
def fact(x):
    if x==1:
        return 1
    else:
        return (x*fact(x-1))
num=5
if num<=0:
    print("enter a positive number!")
else:
    print(fact(num))