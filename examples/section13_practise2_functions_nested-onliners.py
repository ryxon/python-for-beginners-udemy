#print the date/time of the run
humanDate = __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Run at: {humanDate}\n")

def detectType(userinput):
    try:
        returnVal = int(userinput)
        return returnVal, None, None
    except ValueError:
        try:
            returnVal = float(userinput)
            return None, returnVal, None
        except ValueError:
            return None, None, userinput

def splitNones1L(*tuples):
    return [tuple(x for x in tup if x is not None) for tup in tuples]

def splitNones(*tuples):
    return [
        tuple(                  # build a new tuple
            x                   # take element x
            for x in tup        # from each tuple one element at a time
            if x is not None    # filter out None
        )
        for tup in tuples       # outer loop: go through each tuple
    ]

#input 2 numbers in one line, comma seperated
# uInput = input('input 2 numbers (comma seperated): ')
uInput = "aaa  ,bbb  ,ccc ,1,2,3, 3.3,4.5,4.6"
print("uInput:", uInput)

print("\n>>> Breakdown of complex oneliner (from right to left logic):\n ints, floats, strings = splitNones(*zip(*[detectType(x.strip()) for x in uInput.split(',')]))\n")

print("\nx for x in uInput.split(',')")
print( [x for x in uInput.split(',')] )

print("\nx.strip() for x in uInput.split(',')")
print( [x.strip() for x in uInput.split(',')] )

print('\nthis just gets all values from the comma seperated string into a list, removing spaces, \nlets put it in a var')
#better to get these values first, the one-liner gets too complex unnecessary.
csvals = [x.strip() for x in uInput.split(',')]
print("csvals: ",csvals)

dtypes = [detectType(x) for x in csvals]
print('\ndtypes:',dtypes)

zipped = list(zip(*dtypes))
print('\nNow zipping dtypes so the data moves from rows to columns:\n', zipped)

#time to remove the Nones
split = splitNones(*zipped)
print('\nNow splitting the Nones out of the zipped tuples:\n', split)

#and finally unpack the split lists into 3 variables
ints, floats, strings = split
print('\nNow unpacking the split lists into 3 variables:')
print('ints:', ints)
print('floats:', floats)
print('strings:', strings)

print("\n\ncomplete oneliner: splitNones(*zip(*[detectType(x.strip()) for x in uInput.split(',')]))")
ints, floats, strings = splitNones(*zip(*[detectType(x.strip()) for x in uInput.split(',')]))
print(ints, floats, strings)

#one more time seperated in shorter lines without comments+prints
csvals = [x.strip() for x in uInput.split(',')] # get the comma seperated values into a list, removing spaces
dtypes = [detectType(x) for x in csvals] # get the data types of each value into a list of tuples
zipped = list(zip(*dtypes)) # transpose the list of tuples, from rows to columns
ints, floats, strings = splitNones(*zipped) # remove Nones and unpack into 3 variables
print('\nFinally, the same as above but without comments+prints:')
print(ints, floats, strings)