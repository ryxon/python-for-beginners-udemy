print('hello world')

ex_var = 5
ex_float = 30.23
ex_string = 'hello'
ex_bool = True
ex_bool2 = False
ex_list = [1,2,3,4,5]

ex_var = 11

exponentiation = 4**4 # 4^4 = 256
floor_division = 16//5 # 16/5 = 3.2, 16//5 = 3
modulus = 7%3 # 7/3 = 2 remainder 1, 7%3 = 1

def ex_func():
    print('this is an int: '+str(ex_var))
    print('this is a float: '+str(ex_float))
    print('this is a string: '+ex_string)
    print('this is a boolean: '+str(ex_bool))
    print('this is a boolean too: '+str(ex_bool2))

    #this is a list
    print('this is a list: '+str(ex_list))

    return 10

ex_func()

# subtraction operation
subtraction = 5
subtraction -= 2 # subtraction = subtraction - 2
print('subtraction: '+str(subtraction))

#multiplication operation
multiplication = 5
multiplication *= 2 # multiplication = multiplication * 2
print('multiplication: '+str(multiplication))

#division operation
division = 5
division /= 2 # division = division / 2
print('division: '+str(division))

#exponentiation operation
exponentiation = 10
exponentiation **= 2 # exponentiation = exponentiation^2. 10*10 = 100
print('exponentiation: '+str(exponentiation))

#floor division operation
floor_division = 10
floor_division //= 3 # floor_division = floor_division/3. 10/3 = 3.3333, floor_division = 3
#10 is divided by 3, and any leftover decimal value is discarded. so 3.3333 becomes 3

#modulus operation
modulus = 10
modulus %= 3 # modulus = modulus%3. 10/3 = 3 remainder 1, modulus = 1
#10 is divided by 3, and the remainder is 1
#basically chunks of 3 are taken out of 10, until there are no more chunks of 3 left, then the remainder of 1 is returned

#operator precedence
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
expression = (9 - 7)   *   2 ** 3   +   10 % 6   // -1 * 2 - 1
#                2       *   8       +   4       // -1 * 2 - 1
# 2 * 2 = 4
# 2 ** 3 = 8
# 2 * 8 = 16
#---
# 16 (first part of the expression)

# + (lowest precedence so expression is cut into two parts)
# now the next part will be added to 16

# 10 % 6 = 4
# 4 // -1 = -4

# We know that 2 * 3 = 6, so 6 / 3 = 2.
# Similarly, -2 * 3 = -6, so -6 / 3 = -2.
# And 2 * -3 = -6, so 6 / -3 = -2.
# This rule follows the idea that when you reverse an operation (like division), the signs work in a consistent way:
#
# Positive × Positive = Positive
# Negative × Negative = Positive
# Positive × Negative = Negative
# So 4 // -1 has a negative and a positive, so the result is negative. then look at the numbers alone, 4 divided by 1 is 4, then you add the negative sign, so -4

# then -4 * 2 has a negative and positive the same way. which results in -8

# then -8 - 1 = -9

# from the first part of the expression, we have 16
# then 16 - 9 = 7
# done

print('expression: '+str(expression))


