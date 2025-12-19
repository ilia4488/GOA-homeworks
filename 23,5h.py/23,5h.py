# 0)
# .isupper() amowmebs did asoebit aris tu ara texti
# .islower() amowmebs patara asoebit aris tu ara texti
#1)
# samis
# for i in range(5):
#     print(i)

# for i in range(2, 6):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)
#2)
#ki
#list
# fruits = ["apple","pinnapple","melon"]
# for fruit in fruits:
#     print(fruit)
#string
# word = "hello"
# for letter in word:
#     print(letter)
#3)
# words = ["ფორთოხალი","აგურები", "აგური", "ბანანი"]

# a_words = []

# for word in words:
#     if word[0] == ("ა"):  
#         a_words.append(word)

# print(a_words)
#4)
name = input("enter your name")
bname = ""

for nam in name:
    if nam.islower():    
        bname += nam.upper()
    else:
        bname += nam      

print(bname)


# name2 = input("enter your name")
# bname2 = name2.upper()
# print(bname2)




