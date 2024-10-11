#10.107 - Tuples
# Tuples are similar to lists, but they are immutable.
# Tuples are defined using parentheses.
# Tuples are faster than lists.
# Tuples are used to protect data from being modified.
# Tuples are used to store related pieces of information.
# Tuples are used to return multiple values from a function.
# Tuples are used to format strings.
# Tuples are used to store data that doesn't change.
# Tuples are used as dictionary keys.

tuple1 = tuple([123123, 123.123, 12312])
print(tuple1)
tuple2 = tuple("adsasa")
print(tuple2)
tuple3 = tuple([1, 2, 3, 4, 5, 6])
print(tuple3[2])
print(tuple3[2:5])

occupations = {('Angus', 'Young'): 'guitarist',
               ('Brian', 'Johnson'): 'singer',
               ('Malcolm', 'Young'): 'guitarist',
               ('Cliff', 'Williams'): 'bassist',
               ('Phil', 'Rudd'): 'drummer'}
print(occupations['Angus', 'Young'])
# Only way to have a multi-value key in a dictionary is to use a tuple.
# Tuples are used as dictionary keys.
# Tuples are used to store data that doesn't change.

major_cities = ("New York", "Los Angeles", "Chicago", "Houston", "Philadelphia")

for city in major_cities:
    print(city)

print('Now in reverse order:')
backwards = len(major_cities) - 1
while backwards >= 0:
    print(major_cities[backwards])
    backwards -= 1

ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ints[::3]) # (1, 4, 7, 10)
print(ints[1::2]) # (2, 4, 6, 8, 10) # even numbers
print(ints[len(ints)::-1]) # (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

nested = (1, 2, 3, (4, 5, 6), 7, 8, 9, 10, (11, 12, 13))
print(nested[3])
#get index of (11, 12, 13)
index11 = nested.index((11, 12, 13))
print( nested[index11] )
