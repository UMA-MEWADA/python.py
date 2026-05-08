marks = [94 ,4 ,45,6,87,96.9,45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[ :4])
marks.append(5) # add 5 at the end of the list
print(marks)
print(marks.sort()) # returns None because it changes the list in place
print(marks)
print(marks.sort(reverse=True))
print(marks)

list = [ "a", "b", "c", "d", "e"]
print(list.sort(reverse=True))
print(list)

list.insert(1,"u")
print(list)
list.remove("u")
print(list)
list.pop(0)
print(list)