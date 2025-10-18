import operator 

# This simple calculator prompts the user for 2 numbers &
# an arithmetic sign.  Using the operator toolkit, we mapped 
# out the signs in a dictionary, using a try/except block to 
# filter out errors. If all is valid, the result is calculated 
# & returned. If anything is invalid, "unknown value" is returned.

def simple_calc_v2(n1, n2, symbol):
  operation = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
  }

  try:
    if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
      raise TypeError
    
    result = operation[symbol](n1, n2)
  except (KeyError, TypeError, ZeroDivisionError):
    return "unknown value"
  else:
    return result
  
if __name__ == "__main__":
  try:
    first = float(input("Enter Number #1: "))
    second = float(input("Enter Number #2: "))
  except ValueError:
    print("unknown value")
  else:
    op = input("Enter symbol: ")
    print(simple_calc_v2(first, second, op))