num=float(input("Enter the first num"))
num1=float(input("Enter the second num"))
operator=input("Enter the operator (+,-,*,/)")

if operator=="+":
    result=num+num1
    print(f"The result of {num} {operator} {num} is {result}")
elif operator=="-":
    result=num-num1
    print(f"The result of {num} {operator} {num} is {result}")
elif operator=="*":
    result=num*num1
    print(f"The result of {num} {operator} {num} is {result}")
elif operator=="/":
    if num!=0:
        result=num/num1
        print(f"The result of {num} {operator} {num} is {result}")
    else:
        print("Cannot divide by zero")
        result=num/num1
    result=num/num1
    print(f"The result of {num} {operator} {num} is {result}")
else:
    print("Invalid operator")

