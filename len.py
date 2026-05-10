cities = ["Delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]

heroes = ["superman", "batman", "spiderman", "ironman", "hulk"]

print(heroes[0])
print(heroes[1])

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

def print_list(list):
    for item in list :
        print(item, end=" ")
print_list(heroes) 

        
    