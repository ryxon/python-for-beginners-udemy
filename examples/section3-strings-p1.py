# -------------------
# --- 17. STRINGS ---
print("--- 17. STRINGS ---")
# -------------------
ex_1 = 'this is a string'
ex_2 = "this is also a string"
ex_3 = '''this is a string with "quotes" in it'''
ex_4 = """this is a string with 'quotes' in it"""
ex_5 = 'this is a string with \'quotes\' in it'
ex_6 = "this is a string with \"quotes\" in it"
ex_7 = 'this is a string with "quotes" in it'
ex_8 = "this is a string with 'quotes' in it"

# gets index 5 of the string
string = 'orange'
print(string[5])
print("apple"[3])

#string slicing
print("ryanhendriks"[4:])
print("ryanhendriks"[:4])
print("ryanhendriks"[4:8])

#string concatenation
print("hello" + "world")
print("hello" + " " + "world")

concat = "R2" + "-" + "D2"
print(concat)
print(concat[3])
print(concat[1:4]) # 1 to 4, but not including 4. it includes the 1st index and excludes the 4th index

#18. string exercise
print("\n--- 18. string exercise ---")
# -------------------
strvar = "Just do it!"
print(strvar[10])
print(strvar[5:7])
it = strvar[8:]
doit = strvar[5:]
print(it)
print(doit)
print("Don't " + doit)

#20. type() & str()
print("\n--- 20. type() & str() ---")
# -------------------
ex_1 = False
ex_2 = 29
ex_3 = 3.14

strconverted = str(ex_1)

print(type(ex_1))
print(type(ex_2))
print(type(ex_3))

#21. escape characters
print("\n--- 21. escape characters ---")
# -------------------
print("This\tis\ta\tlot\tof\tspace")
print("{:10}{:10}{:10}{:10}{:10}".format("This", "is", "a", "lot", "of space")) # 10 spaces are reserved for each word

#exercise
var_float = 3.14159
print(type(float))
print(str(float) + " is a float")
print("\"Hello, I\'m Ryan, it\'s nice to meet you!\"")
print("*******\n *****\n  ***\n   *")

#26. input()
print("\n--- 26. input() ---")
# -------------------
name = input("What is your name? ")
print("Your name is " + name + ".")

#27. prompt challenge
print("\n--- 27. prompt challenge ---")
# -------------------
name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")
print("So your name is " + name + ", your quest is " + quest + ", and your favorite color is " + color + ".")

#28. int() & float()
print("\n--- 28. int() & float() ---")
# -------------------
user_int = int(input("Enter an integer: "))
print(type(user_int))
user_float = float(input("Enter a float: "))
print(type(user_float))
#get the type of user_float as a string, without the <class '...'>
user_float_type = type(user_float).__name__
print(user_float_type)

ask_integer = int(input("Enter an integer: "))
print("your integer + 10 is: " + str(ask_integer + 10))





