#WHILE loop
from unittest.util import three_way_cmp

number = 0#int(input("Enter a number: "))
sum = 0

while number != 0:
    sum += number
    print(str(sum) + " + " + str(number) + " = " + str(sum))
    number -= 1

print("Loop finished, sum is", sum)

#FOR loop
word = ''#str(input("Enter a word: "))
charcount = 0
for letter in word:
    charcount+=1

print("There are " + str(charcount) + " characters in the word " + word)

#FizzBuzz
for i in range(1, 50):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)


#Factorial
# number = int(input("Enter a number: "))
# factorial = 1
# if number < 0:
#     print("Factorial does not exist for negative numbers")
# elif number == 0:
#     print("Factorial of 0 is 1")
# else:
#     for i in range(1, number + 1):
#         factorial *= i
#     print("The factorial of", number, "is", factorial)


#Range()
print("Range()")
#Range with 1 input
one_input = range(5) #start at 0, end at 5
print(one_input)

for i in one_input:
    print(i)

#Range with 2 inputs
print("Range with 2 inputs")
two_input = range(5, 10) #start at 5, end at 10

for i in two_input:
    print(i)

#Range with 3 inputs
print("Range with 3 inputs")
three_input = range(1, 20, 3) #start at 1, end at 20, increment by 3

for i in three_input:
    print(i)

