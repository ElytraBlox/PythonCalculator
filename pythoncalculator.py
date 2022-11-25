import math
print("Made by ElytraBlox")
print("1-Adding, 2-Subtracting, 3-Multiplying, 4-Dividing, 5-Squaring, 6-Square Rooting, 7-Absolute Value, 8-Smaller Value, 9-Bigger Value, 10-Factorials, 11-Pi Value")
operation = int(input("Choose the operation"))
n1 = int(input("First number"))
n2 = int(input("Second number"))
if operation == 1:
    print(n1+n2)
if operation == 2:
    print(abs(n1-n2))
if operation == 3:
    print(n1*n2)
if operation == 4:
    print(n1/n2)
if operation == 5:
    print(n1**n2)
if operation == 6:
    print(math.sqrt(n1), math.sqrt(n2))
if operation == 7:
    print(abs(n1), abs(n2))
if operation == 8:
    print(min(n1, n2))
if operation == 9:
    print(max(n1, n2))
if operation == 10:
    print(math.factorial(n1), math.factorial(n2))
if operation == 11:
    print(math.pi)






