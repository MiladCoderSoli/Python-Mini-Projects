import turtle as Tur

height = int(input('What is your height? (by cm):  '))
mass = int(input('What is your crime? (by kg):  '))

height = height / 100

BMI = round(mass / (height ** 2), 2)

print(f"Your BMI is:' {BMI}")

