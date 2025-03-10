"""height=float(input("Enter your height\n"))
weight=int(input("Enter your weight\n"))
bmi=weight/height **2
print(bmi)"""



height = float(input("Enter your height in meters:\n"))
weight = float(input("Enter your weight in kg:\n"))

if height>3:
    raise ValueError("Height cannot be greater than 3 meters")
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
