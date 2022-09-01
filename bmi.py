name = input('What is your name? \n')
height = input("enter your height in m \n : ")
weight = input("enter your weight in kg \n: ")

main_height = float(height)
main_weight = float(weight)

first_result = main_weight / main_height **2
result = round(first_result)

if result <= 18.5:
  print(f' {name} Your BMI is {result} you are underweight')
elif result <= 24.9:
  print(f'{name} Your BMI is {result} you have normal weight')
elif result <= 29.9:
  print(f' {name} Your BMI is {result} you are slightly overweight')
elif result <= 35:
  print(f' {name} Your BMI is {result} you are obese')
elif result > 35:
  print(f' {name} Your BMI is {result} you are clinically obese')
else:
  print(f'{result} is not valid') 
  