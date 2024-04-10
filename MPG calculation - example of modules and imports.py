# Python Basics Lesson 4:44

#Import

from random import  randint

#generate random numbers for fuel and miles
fuel = randint (10, 20)
miles = randint(300, 500)

print("The car travel "+ str(miles//fuel)+" miles per gallon.")
print("The car can travel "+str(miles)+ " on a fuel tank.")

