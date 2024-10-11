console = {'nintendo': 'switch', 'sony': 'playstation', 'microsoft': 'xbox'}
print(console['sony'])

print('The '+console['microsoft']+" is the world's worst console.")
print('The '+console['sony']+" however, is the world's best console.")

if 'nintendo' in console:
    print('Nintendo is in the console dictionary.')
else:
    print('Nintendo is not in the console dictionary.')

#9.94 - introduction to dictionaries Excercise
print('\n9.94 - introduction to dictionaries Excercise')
fiveValues = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(fiveValues['c'])
if 'd' in fiveValues:
    print('d is in the dictionary')
else:
    print('d is not in the dictionary')

print('f' not in fiveValues)

#get all keys of the dictionary
keys = fiveValues.keys()
print(keys)
#keys to list
keysList = list(keys)
print(keysList)

#get all values of the dictionary
values = fiveValues.values()
print(values)
#values to list
valuesList = list(values)
print(valuesList)

#get all items of the dictionary, and loop through them
items = fiveValues.items()
print(items)
for key, value in items:
    print(key, value)

print('xbox' in console) # This will return False because xbox is a value, not a key
print('xbox' in console.values()) # Must check in values because xbox is a value, not a key
print('nintendo' in console) # Nintendo is a key, so this will return True

birth_years = {'John': 1980, 'Sally': 1990, 'Tina': 2000, 'Mike': 2010}
# print(birth_years['Johnny']) # This will throw an error because Johnny is not in the dictionary
print(birth_years.get('Johnny')) # This will return None because Johnny is not in the dictionary
print(birth_years.get('Johnny', 'Johnny is not in the dictionary.')) # This will return the message because Johnny is not in the dictionary
print(birth_years.get('Johnny', False)) # This will return the birth year of John because John is in the dictionary
# The second argument in the get method is the default value to return if the key is not in the dictionary

if 'Johnny' in birth_years:
    print('Johnny is in the dictionary.')
else:
    print('Johnny is not in the dictionary.')

#9.97 - dictionaty methods 1 excercise
print('\n9.97 - dictionaty methods 1 excercise')

bands = {"Queen": "Bohemian Rhapsody",
         "Bee Gees": "Stayin' Alive",
         "U2": "One",
         "Michael Jackson": "Billie Jean",
         "The Beatles": "Hey Jude",
         "Bob Dylan": "Like A Rolling Stone"}
print(len(bands))

for key in bands:
    print(key)

bandValues = bands.values()
# convert values to list
bandList = list(bandValues)
print(bandList)

for key, value in bands.items():
    print(key+" - "+value)

print(bands.get("Promise of the Real", "Promise of the Real is not in the dictionary."))

#9.99 - dictionary methods 2
print('\n>>>9.99 - dictionary methods 2')
ex1 = {}.fromkeys(['address'], '123 Main St.')
print(ex1)
ex2 = {'make': 'Ford', 'model': 'Mustang', 'year': 1964}
popped = ex2.pop('year') # pop cuts the key and value from the dictionary and returns the value
print(ex2)
print(popped)

ex3 = ex2.popitem()
print(ex2)
print(ex3) # popitem cuts the last key and value from the dictionary and returns a tuple of the key and value

# 9.100 - dictionary methods 2 excercise
print('\n>>>9.100 - dictionary methods 2 excercise')
consonants = {}.fromkeys('bcdfghjklmnpqrstvwxyz', 'consonant')
for key, value in consonants.items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
bigmac = fast_food_items.pop("McDonald's")
print(fast_food_items)
print(bigmac)
fast_food_items.popitem()
print(fast_food_items)

# 9.102 - dictionary methods 3
print('\n>>> 9.102 - dictionary methods 3')
countries = {1: 'England', 2: 'France', 3: 'Germany', 4: 'Italy', 5: 'Spain'}
print(countries)
countries.clear()
print(countries)

#copy
birth_years = {'John': 1980, 'Sally': 1990, 'Tina': 2000, 'Mike': 2010}
print(birth_years)
birth_years_no_copy = birth_years
birth_years_no_copy['Johnny'] = 2020
print(birth_years)
birth_years.pop('Johnny')
birth_years_copy = birth_years.copy()
birth_years_copy['Johnny'] = 2020
print(birth_years)
print(birth_years_copy)

#update
city_info = {'city': 'New York', 'state': 'New York', 'country': 'USA'}
population = {'population': 8000000}
print(city_info)
city_info.update(population)
print(city_info)
#update state to california
city_info.update(state='California')
print(city_info)

# 9.103 - dictionary methods 3 excercise
print('\n>>> 9.103 - dictionary methods 3 excercise')
internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
print(internet_celebrities)
icelebsCopy = internet_celebrities.copy()
internet_celebrities.clear()
print(internet_celebrities)
print(icelebsCopy)

# 9.104 - dictionary methods 4
print('\n>>> 9.104 - dictionary methods 4')
computers = {'Apple': 'MacBook', 'Dell': 'Inspiron', 'HP': 'Pavilion', 'Microsoft': 'Surface'}
print(computers)
if 'Lenovo' not in computers:
    computers['Lenovo'] = 'ThinkPad'
print(computers)
# setdefault method, does the same as the above if statement in one line
computers.setdefault('Acer', 'Aspire') # Will add Acer to the dictionary with the value Aspire
computers.setdefault('Apple', 'iMac') # Will not add Apple to the dictionary because it is already in the dictionary
print(computers)

# 9.106 - dict()
print('\n>>> 9.106 - dict()')
empty = dict(a=1, b=2, c=3)
print(empty)