# Simple calculator that takes in 2 numbers and an 
# arithmetic sign and filters for non-numeric values.
# If entries pass tests, the result is returned.

def simple_calculator(num1, num2, sign):
  if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
    return "unknown value"
  
  if sign == '+':
    return num1 + num2
  elif sign == '-':
    return num1 - num2
  elif sign == '*':
    return num1 * num2
  elif sign == '/':
    if num2 == 0:
      return "unknown value"
    return num1 / num2

  return "unknown value"

num1 = float(input("Enter number #1:"))
sign = input("Enter sign: ")
num2 = float(input("Enter number #2:"))


print(simple_calculator(num1, num2, sign))