
name = (input('What is your name human?'),
age = input('How old are you (in years)?')
height = float(input("Enter your height (in meters): ")),
weight = float(input('Enter your weight (in kilograms): '))

BMI = weight / (height / 100) ** 2
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")

print(name, 'you are', age, 'years old', 'and your BMI is', f"Your BMI is {BMI}")
