def unusual_five():
    return len("hello")

def other_angle(a,b):
    return 180 - a - b

def area_or_perimeter(l , w):
    if l == w:
        tot = l * w
    else:
        tot = l * 2 + w * 2
    return tot

def simple_multiplication(number) :
    if number % 2 == 0:
       return number *8
    else:
       return number *9