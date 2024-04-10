# Example of Python loops
# Assignnment 6-2, #57
int1 = 10
while int1 > 0 :
    print(int1)
    int1 -= 1

# end of assignment 6-2
# Assignment 6-4 #59

positive_int = int(input("Enter a positive integer:"))
int_init = positive_int
sums = 0
while int_init != 0 :
    sums = sums + int_init
    int_init -= 1
print ("user entered " + str(positive_int) + "." )
print ("The sum found by while loop is "+str(sums)+".")

#assignment 62 --> For loop
word = "hello world"
for letter in word:
    print (letter)

# Assignment 65 Number of Char in a string
string_char = input ("Enter a string : ")
count_char = 0
for letter in string_char:
     count_char += 1
print ("For the string: "+string_char+".")
print("Number Characters = "+str(count_char)+".")
#FizzBuzz Section 6 Assignment 67
int_count = 1
while int_count <= 50:
    if int_count % 3 == 0 and int_count % 5 == 0:
        print (str(int_count)+" is a FizzBuzz")
    elif int_count % 3 == 0:
        print (str(int_count)+"is a Fizz")
    elif int_count % 5 == 0:
        print (str(int_count)+" is a Buzz")
    else:
        print (str(int_count)+" is neither a Fizz not a Buzz")
    int_count += 1

# Assignment 69 - Section 6 Fectorial
fectorial = 1
int_fectorial = int(input("enter an integer value: "))
input_number = int_fectorial
# loop of integers from input number to 1.

while int_fectorial > 1:
        fectorial = (fectorial*int_fectorial)
        int_fectorial -= 1
print ("fectorial of "+str(input_number)+" is: "+str(fectorial))

# Book Solution for the above problem with defined function
  # The argument fac_num's name is short for factorial number.
  def factorial(fac_num):
      # The local variable returned will be used in the for loop used to calculate fac_num's
      # factorial. To do this, it will be multiplied by decrementing values of
      # fac_num. Since it will be multiplied, it was given the initial value of 1.
      returned = 1
      # By the end of this for loop, returned will have been reassigned fac_num's factorial.
      for item in range(fac_num, 1, -1):
          returned *= item

      # returns returned, which now holds the value of fac_num's factorial
      return returned


  print(factorial(3))  # 6
  print(factorial(4))  # 24
  print(factorial(5))  # 120












