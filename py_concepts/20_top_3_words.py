# Returns the top 3 most frequent words in the input text, 
# ignoring non-alphabetic characters & standalone apostrophes. 
# Words are case-insensitive & must contain at least 1 letter.

import re
from collections import Counter

def top_3_words(text):
  t = text.lower() 
  t = re.sub("[^a-z']", " ", t)
  words = re.findall("[a-z']+", t)
  valids = []
  for word in words:
    if word == "'":
      continue
    for c in word:
      if c.isalpha():
        valids.append(word)
        break
  
  counts = Counter(valids).most_common(3)
  matches = []
  for word, count in counts:
      matches.append(word)

  return matches

text = input("Enter words for matching: ")
print(top_3_words(text))