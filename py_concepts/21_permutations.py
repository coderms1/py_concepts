# Returns all possible unique permutations of 
# input string using recursive functionality.

def permutations(input):
  x = len(input)
  result = set()
  if x == 1:
    return [input]
  for i in range(x):
    beg = input[i]
    end = input[:i] + input[i+1:]
    sub_p = permutations(end)
    for j in sub_p:
      result.add(beg + j)

  return list(result)

text = input("Enter a string to permute: ")
p_list = permutations(text)
print(f"All permutations of '{text}': {result}")