#Section 8: Lists
from operator import index

print("\n>> Section 8: Lists <<")

list1 = [1, 2, 3, 4, 5]
list2 = [2.34534, 3.4534, 4.34534, 5.34534, 6.34534]
list3 = ['a', 'b', 'c', 'd', 'e']
list4 = [True, False, True, False, True]
list5 = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
list6 = [1, 2.34534, 'a', True, [1,2,3]]

print( 5 in list1 ) # Check if 5 is in list1 > True
print( 6 in list1 ) # Check if 6 is in list1 > False
print( 1 not in list1 ) # Check if 1 is not in list1 > False

#8.84 introduction to lists exercises
print("\n>> 8.84 introduction to lists exercises <<")
listA = [5, 5.454, True, 'jello', [1,2,3]]
print(listA)

listB = list('PYTHON_RULES_ALOT')
print(listB)
print( 'E' in listB )
print( 'a' in listB )
print( 'A' not in listB )
print( 'A' in listB )

#8.86 indexes and slices exercises
print("\n>> 8.86 indexes and slices exercises <<")
indexes1 = ['carpet', 'hardwood', 'tile', 'concrete', 'linoleum']
print(indexes1[0]) # grabs the 1st element
print(indexes1[1][3]) # grabs the 4th letter of the 2nd element

multiListList = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
print(multiListList[4][2]) # grabs the 3rd element of the 5th list

negative = [1,2,3,4,5,6,7,8,9,10]
print(negative[-1]) # grabs the last element
print(negative[-2]) # grabs the 2nd to last element
print(negative[-3]) # grabs the 3rd to last element

print( listA[1]+31.231 ) # 5.454 + 31.231 = 36.685
print( "i like a " + listA[3] + ' sandwich' ) # i like a jello sandwich

#slicing a list
#negative = [1,2,3,4,5,6,7,8,9,10]
print( negative[:4] ) # [1,2,3,4]
print( negative[0:3] ) # [1,2,3]
print( negative[3:6] ) # [4,5,6]
print( negative[6:] ) # [7,8,9,10]

#re-assiging a list
negative[3] = 123
negative[5:] = [16,17,18,19,110]
negative[-2] = 100
print(negative) # [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#8.87 indexing and slicing exercise
print("\n>> 8.87 indexing and slicing exercise <<")
Elist = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(Elist[0]) # [0, 2]
print(Elist[3][1]) # 14

furniture = ["chair", "table", "desk", "lamp", "bed"]
print(furniture[-5])

print( "Most people own at least "+str(Elist[0][1])+" "+furniture[0]+"s." )

floats = [0.98, 8.76, 6.54, 4.32]
print(floats[1:]) # [8.76, 6.54, 4.32] # prints the 2nd to last elements
print(floats[1:3]) # [0.98, 8.76, 6.54] # prints the 2nd and 3rd elements
print(floats[:2]) # [0.98, 8.76] # prints the first 2 elements

# 8.89 del and list methods
print("\n>> 8.89 list methods <<")
planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
del planets[1]
print(planets) # ['mercury', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
planets.remove('jupiter')
print(planets) # ['mercury', 'earth', 'mars', 'saturn', 'uranus', 'neptune']

#colors blue, red, green, blue, yellow, purple, blue
colors = ['blue', 'red', 'green', 'blue', 'yellow', 'purple', 'blue']
colors.remove('blue') # removes the first instance of 'blue'
print(colors) # ['red', 'green', 'blue', 'yellow', 'purple', 'blue']
colors.append('orange') # adds 'orange' to the end of the list
print(colors) # ['red', 'green', 'blue', 'yellow', 'purple', 'blue', 'orange']

#inserting into a list
colors.insert(2, 'black') # inserts 'black' at index 2
print(colors) # ['red', 'green', 'black', 'blue', 'yellow', 'purple', 'blue', 'orange']

#sorting lists
num_list = [2.718, 4, -19, 10000, 0]
print(num_list)
num_list.sort()
print(num_list) # [-19, 0, 2.718, 4, 10000]
num_list.reverse() # reverses the order of the list
num_list.sort(reverse=True) # sorts in reverse order, does the same as reverse()
print(num_list) # [10000, 4, 2.718, 0, -19]

mixed = [False, 6.56, -2]
mixed.sort() # cannot sort a list with mixed data types
print(mixed)

# Sorting by alphabetical order or ASCIIbetical(words with capital first) order
ASCIIbetical = ['Andy','kiwi', 'apple', 'Karen', 'Brian','banana']
ASCIIbetical.sort() # sorts in ASCIIbetical order, capital letters come first regardless of alphabetical order
print(ASCIIbetical) # ['Andy', 'Brian', 'Karen', 'apple', 'banana', 'kiwi']
ASCIIbetical.sort(key=str.lower) # sorts in alphabetical order
print(ASCIIbetical) # ['Andy', 'apple', 'banana', 'Brian', 'Karen', 'kiwi']

#index method
metals = ['gold', 'silver', 'copper', 'iron', 'tin', 'lead', 'aluminum']
print(metals.index('tin')) # 4
multiple_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
print(multiple_numbers.index(3)) # 2, only returns the first instance of the number

#pop method
print(metals.pop()) # removes the last element of the list and returns it
print(metals.pop(metals.index('copper'))) # removes the 3rd element of the list and returns it
print(metals) # ['gold', 'silver', 'iron', 'tin', 'lead']

#8.90 list methods exercises
print("\n>> 8.90 list methods exercises <<")
arcticAnimals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arcticAnimals[4]
print(arcticAnimals) # ['penguin', 'elephant', 'polar bear', 'walrus', 'reindeer']
arcticAnimals.remove('elephant')
print(arcticAnimals) # ['penguin', 'polar bear', 'walrus', 'reindeer']
arcticAnimals.append('arctic fox')
print(arcticAnimals) # ['penguin', 'polar bear', 'walrus', 'reindeer', 'arctic fox']
arcticAnimals.insert(2, 'snowy owl')
print(arcticAnimals) # ['penguin', 'polar bear', 'snowy owl', 'walrus', 'reindeer', 'arctic fox']
arcticAnimals.sort()
print(arcticAnimals) # ['arctic fox', 'penguin', 'polar bear', 'reindeer', 'snowy owl', 'walrus']
reindeerIndex = arcticAnimals.index('reindeer')
reindeer = arcticAnimals.pop(reindeerIndex)
print(reindeer) # reindeer
print(arcticAnimals) # ['arctic fox', 'penguin', 'polar bear', 'snowy owl', 'walrus']
last = arcticAnimals.pop()
print(last) # walrus
print(arcticAnimals) # ['arctic fox', 'penguin', 'polar bear', 'snowy owl']

#Lists vs. strings
print("\n>> Lists vs. strings <<")
ex_list = [1, 2, 3, 4, 5]
ex_str = 'hello'
ex_list[2] = 15;
#ex_str[2] = 'a'; # cannot change a string in this way
print(ex_list)
print(ex_str)
# you can use parts of a string to create a new string
ex_3 = "No, you can't"
ex_4 = "Yes, you "+ex_3[8:11]
print(ex_4)

# what you cant do with lists
ex_9 = [1, 2, 3, 4, 5]
ex_10 = ex_9 # ex_10 is now a reference to ex_9
ex_10[2] = 15
print(ex_9) # [1, 2, 15, 4, 5]
print(ex_10) # [1, 2, 15, 4, 5]

#how would you make a copy of a list?
print("\n>> Making a copy of a list with .copy() <<")
ex_11 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ex_12 = ex_11.copy()
ex_12[0][2] = 15
ex_11[2] = [17, 18, 19]
ex_12[1] = [14, 15, 16]
print(ex_11) # [[1, 2, 3], [4, 5, 6], [17, 18, 19]]
print(ex_12) # [[1, 2, 15], [14, 15, 16], [7, 8, 9]]

#ex_12 is now a shallow copy of ex_11
#It uses all values of the original list.
#But then has its own specific values when changes are make to inner lists, but not the outer list
#but the structure of the list remains the same
#making changes to ex_11

# What is deepcopy?
from copy import deepcopy
ex_13 = [1, 2, 3, 4, 5]
ex_14 = deepcopy(ex_13)
ex_14[2] = 15
print(ex_13) # [1, 2, 3, 4, 5]
print(ex_14) # [1, 2, 15, 4, 5]

#what is the difference between ex_11.copy() and deepcopy(ex_13)?
#ex_11.copy() is a shallow copy, it only copies the first level of the list
#deepcopy(ex_13) is a deep copy, it copies all levels of the list

#line continuation list vs. string

long_list = ["bush",
             "tree",
             "flower",
             "grass"]
print(long_list)

ex_16 = 2 + \
        3 + \
        4
print(ex_16)

ex_17 = "The \
quick \
brown \
fox"
print(ex_17)
ex_18 = "The " \
        "quick " \
        "brown " \
        "fox"
print(ex_18)

