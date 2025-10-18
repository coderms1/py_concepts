def open_or_senior(data):
  result = []
  for age, handicap in data:
    if age >= 55 and handicap > 7:
      result.append("Open")
    else: 
      result.append("Senior")
  
  return result
  