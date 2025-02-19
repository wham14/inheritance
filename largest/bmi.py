weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

if bmi >=25:
    return "Normal weight"
elif bmi < 30:
    return "Overweight"
else:
    return "Obese"