str1 = "This is a string ." 
str2 = 'create it'
str3 = """ this is a string .\n we creating it in python"""
print(str3)
#concatenation
print(str1 + str2)
#length of string count space and char
print(len(str1))
len2 = len(str3)
print(len2)

#indexing
str5 = "my program"
print(str5[4])

#slicing accesing parts of string

print(str5[0:6]) # 0 index se ek last index kam tak
print(str5[4:len(str5)]) #last index bhi print

#slicing negative index countig  ex apple -5 ,-4 ,-3 ,-2 ,-1
print(str5[-6 : -1])


str6 = "I am studying python"
print(str6.endswith("thon"))##string last me thon hai to true nahi to false endwith(me kuch bhi pas kro jo cheack krna hai)

#capitalize new string creat

str7 = "I am studying python from second year"
print(str7.capitalize())
print(str7)
#replace function
print(str7.replace("python", "java"))

#find function string
print(str7.find("am"))

#count function string

print(str7.count("f"))
