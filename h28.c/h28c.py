def odd_ball(arr):
    i=arr.index('odd')
    if i in arr:
        return True
    else:
        return False
    
def dont_give_me_five(start,end):
    count = 0
    for i in range(start,end+1):
        if "5" not in str(i):
            count = count + 1
    return count

def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr, reverse = True):
        return 'yes, descending'
    else:
        return 'no'
    
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    
    for char in sentence:
        if char in vowels:
            count += 1
            
    return count

def duplicate_encode(word):
    word = word.lower()
    result = ""
    
    for char in word:
        if word.count(char) > 1:
            result = result + ")"
        else:
            result = result + "("
            
    return result
