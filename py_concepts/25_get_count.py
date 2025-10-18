# This simple program counts the vowels in a 
# user-inputted sentence and returns the count.

def get_count(sentence):
    count = 0
    for i in sentence:
        if i.lower() in 'aeiou':
            count += 1
    
    return count

inputstr = input("Please enter sentence for vowel counting: ")
print(get_count(inputstr))