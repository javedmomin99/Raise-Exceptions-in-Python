height = float(input("Height in metre : "))
weight = float(input("Weight in kg: "))

if height > 3:
  raise ValueError("Human Height should not be greater than 3 metres")
elif weight > 1000:
  raise ValueError("Human Weight should not be greater than 1000 Kgs")
else:
  bmi = weight / height ** 2
  print(f"BMI = {bmi}")
