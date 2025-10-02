#zip example, combining two lists into a list of tuples, combined by index
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
zipped = zip(list1, list2)
print("\n>>> Example of zip function:")
print("list1:", list1, "\nlist2:", list2)
print("Combined by zip():")
print(list(zipped))
#explaining * operator
print("\n>>> Example of * operator:")
print("list1:", list1)
print("Using *list1 in print():")
print(*list1)
item1, item2, *rest = list1
print("Using *list1 in variable assignment:")
print("item1:", item1)
print("item2:", item2)
print("rest:", rest)
# explaining ** operator
def exampleFunc(param1, param2, param3):
    print(f"param1: {param1}, param2: {param2}, param3: {param3}")
dict1 = {'param1': 'value1', 'param2': 'value2', 'param3': 'value3'}
print("\n>>> Example of ** operator:")
print("dict1:", dict1)
print("Using **dict1 in function call:")
exampleFunc(**dict1)


params1 = {"one": "gdgwet34", "two": "98wehg98er", "three": "ASDASD"}
print(params1)
print(*params1)


quit()

# Lists → mutable, ordered, allow duplicates.
#
# Tuples → immutable, ordered, allow duplicates.
#
# Sets → mutable, unordered, unique elements.
#
# dict → like a set has curly brackets, but a named index. curly brackets without an index is a set.

#explain tuple()
print("\n>>> Example of tuple():")
list3 = [10,20,30]
tuple1 = tuple(list3)
print("list3:", list3)
print("tuple1 (converted from list3 using tuple()):", tuple1)
print(tuple1[0])
print(list3[0])

print("\n>>> Example of list():")
#A list is mutable, you can change its content by assignment
list3[0] = 100
#remove item by value
list3.remove(20)
#but it doesnt have .add() method, it has .append()
list3.append(40)
#it also has .extend() to add multiple items
list3.extend([50,60])
#what about prepending? use .insert(), you must provide the index
list3.insert(0,6)
print("list3 after changes:", list3)
#can you also prepend to it without using .insert()? yes, with slicing
list3[0:0] = [1,2,3,4,5]
print("list3 after prepending with slicing:", list3)
#you can also use + operator to concatenate lists
list4 = [70,80,90]
list5 = list3 + list4
print("list5 (list3 + list4):", list5)

print("\n>>> Example of tuples:")
#A tuple is immutable, you cannot change its content by assignment
tuple1 = (10,20,30)
print("tuple1:", tuple1)
# tuple1[0] = 100 # this will throw an error
#tuple doesnt have .remove() method, it has .count() and .index()
print("tuple1 count of 20:", tuple1.count(20))
print("tuple1 index of 30:", tuple1.index(30))
#tuple doesnt have .append() or .extend() method, but you can concatenate tuples with +
tuple2 = (40,50,60)
tuple3 = tuple1 + tuple2
print("tuple3 (tuple1 + tuple2):", tuple3)
#you can also use * operator to repeat tuples
tuple4 = tuple1 * 2
print("tuple4 (tuple1 * 2):", tuple4)
#you can convert tuple to list and vice versa
list6 = list(tuple1)
print("list6 (converted from tuple1 using list()):", list6)
#you can convert string to list or tuple
str1 = "hello"
list7 = list(str1)
tuple5 = tuple(str1)
print("str1:", str1)
print("list7 (converted from str1 using list()):", list7)
print("tuple5 (converted from str1 using tuple()):", tuple5)
#you can convert list or tuple to string using .join()
str2 = ''.join(list7)
str3 = ''.join(tuple5)
print("str2 (converted from list7 using .join()):", str2)
print("str3 (converted from tuple5 using .join()):", str3)
#you can also use .join() with a separator
str4 = '-'.join(list7)
print("str4 (converted from list7 using .join() with '-'): ", str4)

print("\n>>> Example of sets:")
#A set is mutable, you can change its content by assignment
set1 = {1,2,3,4,5}
print("set1:", set1)
#you can add items to a set using .add()
set1.add(6)
print("set1 after adding 6:", set1)
#you can remove items from a set using .remove() or .discard()
set1.remove(3)
set1.discard(4)
print("set1 after removing 3 and discarding 4:", set1)
#you can also use .pop() to remove and return an arbitrary item
popped_item = set1.pop()
print("set1 after popping an item:", set1)
print("popped item:", popped_item)
#you can use .clear() to remove all items from a set
set1.clear()
print("set1 after clearing:", set1)
#you can create a set from a list or tuple using set()
list8 = [1,2,2,3,4,4,5]
tuple6 = (5,6,6,7,8,8,9)
set2 = set(list8)
set3 = set(tuple6)
print("list8:", list8)
print("set2 (converted from list8 using set()):", set2)
print("tuple6:", tuple6)
print("set3 (converted from tuple6 using set()):", set3)

#own testing
dlist1 = list8 + list(tuple6)
print(dlist1)
#turning dlist1 with duplicates into a set for filtering
dset1 = set(dlist1)
print(dset1)
#now back to list without duplicates
noduplist1 = list(dset1)
print(noduplist1)

