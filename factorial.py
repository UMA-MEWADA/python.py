n = 5

def calculate_factotial(n):
    fact = 1
    for i in range(1 , n+1):
        fact*= i 
        print(fact)
        
calculate_factotial(6)

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD = ", inr_val,  "INR")
    
converter(100)