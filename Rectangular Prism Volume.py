# Python Basics - Excercise 4-37
length = int(input("Enter an integer that represent length in inch: "))   #length of rectangular prism
width = int(input("Enter an integer that represent width in inch: "))  # width of rectangular prism
height = int(input("Enter an integer that represent height in inch: "))   # height of rectangular prism
def prism_volume (l,w,h): # define function for prism volume
    return l * w * h

print("The Volume of rectangualar Prism is "+str(prism_volume(length, width,height))+" cubic inch.")

