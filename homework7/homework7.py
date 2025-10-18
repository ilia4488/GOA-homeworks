# #0) ლოგიკური ოპერატორები Python-ში

# "and" — ნიშნავს "და"
# აბრუნებს True მხოლოდ მაშინ, როცა ორივე პირობა ჭეშმარიტია
a = 5
b = 10
print(a > 2 and b > 5)   # True, ორივე პირობა მართალია

# "or" — ნიშნავს "ან"
# აბრუნებს True, თუ მაინც ერთი პირობა მართალია
print(a > 10 or b > 5)   # True, რადგან მეორე პირობა მართალია

# "not" — ნიშნავს "არა"
# ამოატრიალებს შედეგს — True ხდება False და პირიქით
print(not(a > 2))        # False, რადგან a > 2 მართალია, ხოლო not საპირისპიროს დაწერს

# #1
print(5>2)
print(10<20)
print(10>7+2)

print(2>5)
print(20>30)
print(1<1)

# #2
print(True or False)
print(not False)
print(True or True)

print(False or False)
print(True and False)
print(not True)
#3
(True and not False) or (False and True) or (not (False or False) and True) and (True or not (False and True))
(True) or (False) or (True) and (True)
(True)
#4
(15 + 5 > 10 * 2 and 50 / 5 == 10 or 7 - 2 >= 6) and not (20 < 10 + 15 and 9 / 3 == 2 or 8 - 3 < 2) or (30 / 3 == 10 and (14 - 4 > 5 + 5 or 6 * 2 == 11)) and (40 == 39 + 1 or 12 / 4 != 3)
(False and not (True) or False and True)
(False)