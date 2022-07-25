height = input("enter your height in cm: ")
weight = input("enter your weight in kg: ")



float_height = float(height)
float_weight = float(weight)

BMI = float_weight / ( float_height * float_height)
print(int(BMI))
