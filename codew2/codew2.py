def filter_list(l):
  result = []
  for i in l:
    if type(i) == int:
      result.append(i)
  return result
  

def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i*i
    return sum

def friend(x):
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names

def lovefunc( flower1, flower2 ):
    if (flower1 %2 == 0 and flower2 %2 == 1) or (flower1 %2 == 1 and flower2 %2 == 0):
        return True
    else:
        return False
    
def disemvowel(string_):
    vowels = "aeiouAEIOU"  # include uppercase vowels too
    result = ""
    for i in string_:
        if i not in vowels:
            result = result + i
    return result