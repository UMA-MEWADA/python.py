collection = {1 , 2, 3, 3 ,"hello" ,"world ", 1.7} # print without duplicates
# set element are not mutable but we can add or remove elements from the set ,set are muttable.
# sets are unordered collections of unique elements
print(collection)
print(type(collection))
print(len(collection))

collection =set() # to create an empty set
print(type(collection))

collection.add(5)
collection.add("python")
collection.add(( 10 , 44, "java"))
collection.remove(5)
collection.clear() # to remove all added elements from the set 
print(collection)
