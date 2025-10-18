# Takes in an integer and returns whether it's a
# square or not (True or False)
import math
def squareOfSquares(i):
  if i < 0:
    return False
  sqrt = math.isqrt(i)
  return sqrt**2 == i

print(squareOfSquares(4))
print(squareOfSquares(3))
print(squareOfSquares(0))