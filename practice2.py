#3. Write a Python Program to calculate your Body Mass Index?
height = float(input("Enter your height(m): "))
weight = float(input("Enter your weight(kg): "))
print("Your BMI is: ", round(weight / (height * height), 2))