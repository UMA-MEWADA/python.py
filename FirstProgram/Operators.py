#Arithmetic operators
a = 5 
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #a^b

# Relational / comparison operators
A = 50 
B = 20

print(A == B) # output flase
print(A != B) # output true
print(A >= B) # output true
print(A > B) # output true
print(A <= B) # output false
print(A < B) #output false

# Assignment operators
num = 10 
# num = num + 10 #  output 10+10 = 20
num+= 10 # output 20
print("num :", num) 

num2 = 10 
num2-= 10 # output 0
print("num2 :", num2)

num3 = 10 
num3*= 10 # output 100
print("num3 :", num3)


num4 = 10 
num4/= 10 # output 1.0
print("num4 :", num4)

num5 = 10 
num5%= 10 # output 0
print("num5 :", num5)

# logical operators ( not , and , or)
N = 50 
V = 30
print(not False) # output True
print(not True ) # output False
print(not (N > V) ) # output False

# and operator
val1 = True
val2 = True
print("and operator :", val1 and val2) #output true
val3 = True
val4 = False
print("AND operator :", val3 and val4) #output false

# or operators
Val1 = True
Val2 = True
print("OR operator :", Val1 or Val2) #output true

vaL3 = 50
vaL4 = 40
print("OR operator :", (vaL3 == vaL4) or (vaL3 > vaL4)) #output true
val5 = False
val6 = False
print("OR operator :", val5 or val6) # output false