#Section 11.110: Sets & compihensions
#sets are unordered collections of unique elements
#sets are defined by curly braces
#sets are mutable
#sets are unordered
#sets are iterable

set1 = {1, 2, 3, 4, 5}
set2 = set({'a', 'b', 'c', 'd', 'e'})
print(set1)
print(set2)

set3 = set(range(1,12,2))
print(set3)

set4 = set('hello')
print(set4)

print(7 in set3)

olympic_cities = {'London', 'Beijing', 'Athens', 'Sydney', 'Atlanta',
                  'Barcelona', 'Seoul', 'Los Angeles', 'Moscow', 'Montreal',
                  'Munich', 'Mexico City', 'Tokyo', 'Rome', 'Melbourne',
                  'Helsinki', 'London', 'Stockholm', 'Paris', 'Amsterdam'}

ol = olympic_cities

ol.add('Rio de Janeiro') # This will add Rio de Janeiro to the set
print(ol)

ol.remove('Stockholm')
# ol.remove('Stockholm') # This will throw an error because Stockholm is not in the set
print(ol)

ol.discard('Stockholm')
ol.discard('Stockholm') # This will not throw an error because Stockholm is not in the set
print(ol)

fruits = {'apple', 'banana', 'cherry', 'apple'}
print(fruits) # This will only print apple once because sets only contain unique elements

set5 = fruits.copy()
print(set5)

ints1 = {1, 2, 3, 4, 5}
ints2 = {4, 5, 6, 7, 8}
union = ints1.union(ints2) # combines the two sets
print(union) # This will print {1, 2, 3, 4, 5, 6, 7, 8}
union2 = ints1 | ints2 # combines the two sets
print(union2) # This will print {1, 2, 3, 4, 5, 6, 7, 8}

intersection = ints1.intersection(ints2) # finds the common elements between the two sets
print(intersection) # This will print {4, 5}
intersection2 = ints1 & ints2 # finds the common elements between the two sets
print(intersection2) # This will print {4, 5}

difference = ints1.difference(ints2) # finds the elements that are in ints1 but not in ints2
print(difference) # This will print {1, 2, 3}
difference2 = ints2.difference(ints1) # finds the elements that are in ints2 but not in ints1
print(difference2) # This will print {8, 6, 7}
difference3 = ints1 - ints2 # finds the elements that are in ints1 but not in ints2
print(difference3) # This will print {1, 2, 3}
difference4 = ints2 - ints1 # finds the elements that are in ints2 but not in ints1
print(difference4) # This will print {8, 6, 7}


#set comprehension
set6 = {x for x in range(10)}
print(set6)

ALLCAPS = {x.upper() for x in ['apple', 'banana', 'cherry']}
print(ALLCAPS)

range1 = range(10, 0, -1)
#turn range into a list
list1 = list(range1)
print(list1)

range1 = [x+5 for x in range1]
print(range1)

