# Takes two arrays, combines them and
# sorts them in ascending order.

def merge_arrays(arr1, arr2):
  arr3 = arr1 + arr2
  result = set(arr3)

  return sorted(result)

arr1 = [2,4,6,8,9]
arr2 = [1,2,3,4,5]

print(merge_arrays(arr1, arr2))