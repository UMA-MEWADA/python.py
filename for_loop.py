num = [1 , 2 ,3 ,4 ,5]
for i in num:
    print(i)
    
 # second example   
fruit = ["apple", "banana", "grapes", "orange"]
for val in fruit:
    print(val)
    
 #third example foor loop
string = "hello world"
for char in string:
    print(char) 

# fourth example for loop
str = "python programming"
for char in str:
    if(char == 'n'):
       print("n found")
       break
    print(char)
else:
    print("end of loop")  
    
# fifth example for loop

nums = (1,4,9,16,25,36,49,64,81,100) 
x = 49

idx = 0    
for el in nums:
    if(el == x):
        print("number found at index", idx)
        break
    idx += 1
    
# sixth example for loop in range funcction
   
seq = range(5)

for i in seq:
    print(i)   

# ya six ko ese bhi likh sakte hain

for i in range(5):
    print(i)      
    
# rangr function ke 3 parameters hote hain start, stop, step        
for i in range(0, 10, 2): 
    print(i) #first and third parameter optional
    
# example for even numbers print    

for i in range(2, 101, 2):
    print(i)
    
# example for odd numbers print

for i in range(1 , 100 , 2):
    print(i)    
    
# Dincrising order print

for i in range(100 , 0 , -1):
    print(i)   
    
#multiples table print   
n = int(input("enter the number :"))
for i in range(1, 11):
    print(i*n) 
