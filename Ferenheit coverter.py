Celsius = int(input("Enter the temperature as integer in celsius:"))

def Ferenheit (C):
    return (18 * Celsius + 320)/ 10


    # To avoid the approximation error that would occur if the float 1.8 was used in the calculation, 1.8 * 10 is used
    # instead, resulting in the integer 18.  To balance this out, 32 is also multiplied by 10 to get 320.  After the
    # calculations in the parentheses are finished, the result is divided by 10, which gives the correct Fahrenheit

print("The Fahrenheit equivalent of "+str(Celsius)+" degrees Celsius is "+str(Ferenheit(Celsius))+" Ferenheit.")

# use of round () for the ferenheit conversion
Celsius2 = int(input("Enter the temperature as integer in celsius:"))

def Ferenheit (C):
    return round((1.8 * Celsius2 + 32),1) #round to 1 digit

print("The Fahrenheit equivalent of "+str(Celsius)+" degrees Celsius is "+str(Ferenheit(Celsius))+" Ferenheit.")
