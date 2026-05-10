subjects = {
    "python" , "java" , "c++" ,"python", "javascript" , "java" , "python" ,"java ", "c++" ,"c"
}
print(subjects)
print(len(subjects))
print(type(subjects))

""" second program store marks of 3 subjects in a empty dictionary and print the dictionary key value pairs """

marks = {}
  
x = int(input("Enter phy : "))
marks.update({"phy" : x}) 

x = int(input("Enter chem : ")) 
marks.update({"chem" : x}) 

x = int(input("Enter maths : "))
marks.update({"maths" : x})

print(marks)