#5. Write a Python Program for cube sum of first n natural numbers?
def csm(n):
    return n ** 3


sum = 0
n = int(input("enter the number upto which you want to find the cube sum: "))
if n < 0:
    print("enter a positive number!")
else:
    for i in range(n):
        sum = sum + csm(i)
print(sum)