number = int(input('Please insert a number between 1 and 10: '))
# roman equivalent in a match case statement
match number:
    case 1: print('I')
    case 2: print('II')
    case 3: print('III')
    case 4: print('IV')
    case 5: print('V')
    case 6: print('VI')
    case 7: print('VII')
    case 8: print('VIII')
    case 9: print('IX')
    case 10: print('X')
    case _: print('You did not enter a number between 1 and 10.')

# do the same in elif statements
if number == 1:
    print('I')
elif number == 2:
    print('II')
elif number == 3:
    print('III')
elif number == 4:
    print('IV')
elif number == 5:
    print('V')
elif number == 6:
    print('VI')
elif number == 7:
    print('VII')
elif number == 8:
    print('VIII')
elif number == 9:
    print('IX')
elif number == 10:
    print('X')
else:
    print('You did not enter a number between 1 and 10.')



usernum = int(input('Please insert a number: '))
if usernum == 0:
    print('You entered 0.')
elif usernum < 0:
    print('You entered a number below ZERO.')
elif 0 < usernum <= 100:
    print('You entrered something between 0 and 100.')
else:
    print('The number is above 100!!')




#Grade determination
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

#simulate switch/case in python
match grade:
    case grade if grade >= 90:
        print("A")
    case grade if grade >= 80:
        print("B")
    case grade if grade >= 70:
        print("C")
    case grade if grade >= 60:
        print("D")
    case _:
        print("F")




#student loan eligibility
gpa = float(input("What was the applicant's Grade Point Average? "))
inst_app = input("Is the student going to be educated at an approved institution? ")
if gpa >= 3.7:
    if inst_app == "yes":
        print("This applicant is eligible for a scholarship.")
    else:
        print("This applicant is not eligible since they are not going to an approved institution.")
else:
    print("This applicant did not have a high enough GPA.")



# --- Flow Control: if, elif, else
veg = input("Enter a vegetable: ")
if veg == "carrot":
    print("I like carrot")
elif veg == "potato":
    print("I like potato")
else:
    print("I don't like", veg)

#continiously check the input
while True:
    veg = input("Enter a vegetable: ")
    if veg == "carrot":
        print("I like carrot")
        break
    elif veg == "potato":
        print("I like potato")

        rawBaked = input("Do you like it raw or baked? ")
        if rawBaked == "raw":
            print("I like raw potato")
        elif rawBaked == "baked":
            print("I like baked potato")
        else:
            print("I don't like", rawBaked)

    else:
        print("I don't like", veg)






