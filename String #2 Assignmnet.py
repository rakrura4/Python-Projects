#Section 7 assignmnet 57 String - 2
#Assignmnet 57
mixed_case = "A Song of Ice and Fire"
print(mixed_case.islower())
print(mixed_case.isupper())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith("A"))
print(mixed_case.endswith("e"))
word = mixed_case.split(" ")
print(word)
print("".join(word).isalpha())
# Assignment 60 string method exercise
the_string = "North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17,"*"))
center_plus = the_string.center(16,"+")
print(center_plus)
print(the_string.lstrip("North"))
print(center_plus.rstrip("+"))
print(center_plus.replace("North", "South"))

#assignment 78 - string reversal
inp_string = input("enter a string :")
rev_string = ""
char_count = 0
for letter in inp_string:
    rev_string=letter+rev_string
    char_count += 1
print(rev_string)

#Book solution for reverse string
user_string = input("Please enter a string.")
reversed = ""

for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]

print(reversed)
# Assignment #80 word count

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

def word_count(words):
    word_string=""
    word_count1 = 1

    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            word_string += i
    print(word_string)

    for j in word_string:
        if j == " ":
            word_count1 += 1
    return word_count1

print (word_count(str_1))
print(word_count(str_2))
print (word_count(str_3))

#book Solution for #80 word counts
str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."


# This function reduces the string to letters, numbers, spaces, hyphens, and apostrophes, and assigns that string to
# the variable spaces_and_letters so that the number of words in it can by found by counting spaces between words.
def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            spaces_and_letters += i
    for j in spaces_and_letters:
        if j == " ":
            word_count += 1
    return word_count


print(word_counter(str_1))
print(word_counter(str_2))
print(word_counter(str_3))

#list slicing excercise #87
list_slice = [[0,2],[4,6],[8,10],[12,14]]
print(list_slice [0])
print (list_slice [-1][-1])

furniture = ["chair", "table", "desk", "lamp" "bed"]
print(furniture[-4])
print ("Most people own at least "+ str(list_slice[0][1])+" "+furniture[0]+"s.")
slice_float = [0.98, 8.76, 6.54, 4.32]
print (slice_float [1:])
print (slice_float[1:3])
print (slice_float[:2])
#assignment 90 - del append
artic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del artic_animals[4]
print(artic_animals)
artic_animals.remove("elephant")
artic_animals.append("artic fox")
artic_animals.insert(2,"snowy owl")
artic_animals.sort()
print(artic_animals)
print (artic_animals.index("reindeer"))
print(artic_animals.pop())
