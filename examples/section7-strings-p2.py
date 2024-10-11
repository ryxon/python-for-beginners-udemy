def p(param):
    print(param)

# Strings upper and lower case
print( "> Strings upper and lower case" )
lowerCase = 'sdfgkhdfsgjkhdsgf'
print( lowerCase.upper() )
upperCase = 'SDFGKHDFSGJKHDSGF'
print( upperCase.lower() )
print( upperCase.isupper() )
print( lowerCase.islower() )
print( upperCase.islower() )

#isalpha, isalnum, isdecimal
print( "\n> isalpha, isalnum, isdecimal" )
print( "Batman".isalpha() )
print( "Batman123".isalpha() )
print( "Batman".isalnum() )
print( "Batman123".isalnum() )
print( "Batman".isdecimal() )
#isspace
print( "\n> isspace" )
print( " ".isspace() )
print( "      ".isspace() )

#istitle
print( "\n> istitle" )
print( "batman".istitle() )
print( "Batman".istitle() )

#startswith and endswith
print( "\n> startswith and endswith" )
print( "Batman".startswith("Bat") )
print( "Batman".endswith("man") )

#joining strings
print( "\n> joining strings" )
print( ", ".join(["Batman", "Superman", "womenwoman", "Flash"]) )
print( " ".join(["Batman", "Superman,", "womenwoman", "Flash"]) )
heroes = ", ".join(["Batman", "Superman", "womenwoman", "Flash"]).split(", ")
print( heroes )

#LOOP through heroes
print( "\n> LOOP through heroes" )
for hero in heroes:
    print( hero )

#String methods 1 excercise
print( "\n> String methods 1 excercise" )
mixed_case = "A Song of Ice and Fire"
print( mixed_case.isupper() )
print( mixed_case.islower() )
print( mixed_case.upper() )
print( mixed_case.lower() )
print( mixed_case.istitle() )
title_case = mixed_case.title()
print( title_case )
print( mixed_case.startswith("A") )
print( mixed_case.endswith("Fire") )
words = mixed_case.split(" ")
print( words )
print( "".join(words).isalpha() )
print( " ".join(words) )
print( " - ".join(words) )

#String methods 2
print( "\n> String methods 2" )

#rjust and ljust
print( "\n> rjust and ljust and center" )
hellow = "Hello Worlds"
print( hellow.ljust(20,'.') )
print( hellow.rjust(20,'.') )
print( hellow.center(20,'.') )

#strip, lstrip, rstrip
print( "\n> strip, lstrip, rstrip" )
print( "    Hello    ".strip() )
print( "    Hello    ".lstrip() )
print( "    Hello    ".rstrip() )

print('juice, bread, cheese, beef, bread'.strip(', '))
print('juice, bread, cheese, beef, bread'.strip(', bread'))
print('blueblueyellowblue'.strip('eubl'))

p('juice, bread, cheese, beef, bread'.strip(', '))

#String methods 2 + exercise
print( "\n> String methods 2 + exercise" )
the_string = "North Dakota"
print( the_string.rjust(17) )
print( the_string.ljust(16,'*') )

center = the_string.center(16,'+')
print( center )

print( center.lstrip('+') )
print( center.rstrip('+') )
print( center.strip('+') )
print( the_string.replace("North", "South") )

#len()
print( "\n> len()" )
print( len("Hello") )
longword = "Supercalifragilisticexpialidocious"
print( len(longword) )
print( len(longword[7:33]) )

#78. Challenge string reverser
print( "\n> Challenge string reverser" )
userString = input("Enter a string to be reversed: ")
reversedString = ''

print( range(len(userString) - 1, -1, -1) ) #range is a lazy object, so it needs to be converted to a list or looped through
print( list(range(len(userString) - 1, -1, -1)) )

for i in range(len(userString) - 1, -1, -1):
    reversedString += userString[i]

print( reversedString )

#80. Word counter excercise
print( "\n> Word counter excercise" )

def wordCount(sentence):
    words = sentence.split(" ")
    print(len(words))


sentence = input("Enter a sentence: ")
wordCount(sentence)

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."
wordCount(str_1)
wordCount(str_2)
wordCount(str_3)

#82. Format()
name = "James"
degree = "PhD"
field = "Data Science"
title = "Data Scientist"
experience = 3
print( "{} has a {} in {} and is a {} with {} years of experience.".format(name, degree, field, title, experience) )