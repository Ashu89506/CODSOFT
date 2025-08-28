# CALCULATOR
def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2  
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2
def avg(num1,num2):
    return (num1 + num2) / 2
print("Select operation: \n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Average")
select = input("Enter choice(1,2,3,4,5): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if select == '1':
   print(f"Sum of {num1} and {num2} is :",add(num1,num2))
elif select == '2':
    print(f"Difference of {num1} and {num2} is :",subtract(num1,num2))
elif select == '3':
    print(f"Product of {num1} and {num2} is :",multiply(num1,num2))
elif select == '4':
    if num2 != 0:
        print(f"Division of {num1} and {num2} is :",divide(num1,num2))
    else:
        print("ZeroDivisionError.")
elif select == '5':
    print(f"Average of {num1} and {num2} is :",avg(num1,num2)) 
else:
    print("Invalid Opration")