year=int(input("enter a year"))

if year % 4 and year % 100 != 0:
    print("leap year")
else:
    print("not leap year")