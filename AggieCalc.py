#Ooremide Adegbola
#AggieCalc
#9/28/22

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

print("Which Operation would you like to peform?")
method = (input("+, -, *, /: "))

result = 0
if method == '+':
    result = num1 + num2 
elif method == '*':
    result = num1 * num2 
elif method == '/':
    result = num1 / num2
elif method == '-':
    result = num1 - num2 
else:
    print("Invalid Operator!")

print(num1, method, num2, ":", result)


