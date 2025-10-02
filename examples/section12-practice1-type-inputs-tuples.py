def detectType(userinput):
    try:
        returnVal = int(userinput)
        return returnVal, 'int'
    except ValueError:
        try:
            returnVal = float(userinput)
            return returnVal, 'float'
        except ValueError:
            return userinput, 'str'

while True:
    try:
        userinput = input("Enter something: ")
        inputType = ''

        #check if input is an integer or float or string, without throwing an error
        # if userinput.isdigit():
        #     userinput = int(userinput)
        #     inputType = 'int'
        # elif userinput.replace('.','',1).isdigit() and userinput.count('.') < 2:
        #     userinput = float(userinput)
        #     inputType = 'float'
        # else:
        #     userinput = str(userinput)
        #     inputType = 'str'

        convertedInput, inputType = detectType(userinput)


        print(f"you entered a {inputType}: {convertedInput}")

        #only works with integers and otherwise throws intentional type error
        result = convertedInput + 10
        print(f"your input + 10 is: {result} and the type is {type(result)}")



        break  # Exit loop if conversion is successful
    except ValueError:
        print("That is not a valid integer. Please try again.")
    except TypeError:
        print("Wrong type entered, should be int or float. Please try again.")



