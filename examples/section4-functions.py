#scopes
example = "global value"
def loc_ex():
    example = "local value"
    print(example)
print(example)
loc_ex()




# basic import, must use random.functionname
# import random
# print(random.randint(1, 1000))

# imports the randint function from the random module
from random import randint

# imports all functions from random without having to use random.function
from random import *

print(randint(1, 1000))

def MilesPerGallon(miles, gallons):
    #floor division
    return miles // gallons

# inputMiles = int(input('Enter miles driven: '))
# inputGallons = int(input('Enter gallons used: '))

#input miles but only allow between 10 and 25
inputMiles = int(input('Enter miles driven(between 200 and 400): '))
while inputMiles < 200 or inputMiles > 400:
    print("Miles must be between 200 and 400")
    inputMiles = int(input('Enter miles driven(between 200 and 400): '))

#input gallons but only allow between 200 and 400
inputGallons = int(input('Enter gallons used(between 10 and 25): '))
while inputGallons < 10 or inputGallons > 25:
    print("Gallons must be between 10 and 25")
    inputGallons = int(input('Enter gallons used(between 10 and 25): '))


print("Miles per gallon: " + str(MilesPerGallon(inputMiles, inputGallons)))



exit()
# --- Section 4: Functions ---
def greet(param1='no param1', param2='no param2'):
    return param1 + ' ' + param2


greeting = greet('Hello', 'world')
print(greeting)
print(greet())

# name = input('Enter your name: ')
# print(greet('Hello', name))

prismmetrics = input('input height, length and width (comma seperated): ')

#short for loop
#prismArray = [x.strip() for x in prismmetrics.split(',')]

#easier to read loop
prismArray = []
for x in prismmetrics.split(','):
    stripped_value = x.strip()
    prismArray.append(stripped_value)


height = int(prismArray[0])
length = int(prismArray[1])
width = int(prismArray[2])

def volume(height, length, width):
    return height * length * width

print("The volume of the prism is: " + str(volume(height, length, width)) + " cubic units")

# USING INT, must account for approximation error
# celc = round(float(input('Enter Celcius temperature: ')), 1)
#
# def farenheit(celc):
#     faren = (1.8 * celc + 32)
#     #count to 1 decimal place
#     return round(faren, 1)
#
# print("Celcius: " + str(celc) + " is " + str(farenheit(celc)) + " in Farenheit")
#
#
# def fahrenheit(cel):
#     # To avoid the approximation error that would occur if the float 1.8 was used in the calculation, 1.8 * 10 is used
#     # instead, resulting in the integer 18.  To balance this out, 32 is also multiplied by 10 to get 320.  After the
#     # calculations in the parentheses are finished, the result is divided by 10, which gives the correct Fahrenheit
#     # temperature.
#     return (18 * cel + 320) / 10
#
#
# print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")




