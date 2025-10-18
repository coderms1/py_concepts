# Takes a number and adds all numbers  
# from 1-to-num and returns result

def summation(num):
  total = 0
  if num <= 0:
    return "Must be a positive whole number."
  for i in range(num):
    total += (i + 1)

  return total

inputNbr = int(input("Enter number for grasshopper: "))
print(summation(inputNbr))