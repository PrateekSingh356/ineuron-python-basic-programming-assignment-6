#1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
def fibbo(fibb):
    if fibb<=1:
        return fibb
    else:
        return (fibbo(fibb - 1) + fibbo(fibb - 2))

fibb = int(input("enter the number of fibbonacci numbers: "))
if fibb<0:
    print("enter a positive number!")
else:
    for i in range(fibb):
        print(fibbo(i))