# Day 2: 30 Days of python programming 

first_name = 'Kaden'
last_name = 'Nelson'

print("First name length: ", len(first_name))
print("Last name length: ", len(last_name))

# Step 4

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one 
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one 
exp = num_one ** num_two
floor_divison = num_one // num_two

print(total, diff, product, division, remainder, exp, floor_divison)

# Area of circle 

radius = 30

def AreaOfCircle(radius): 
    pi = 3.1415926
    area = radius ** 2 * pi
    return area 

area = AreaOfCircle(radius)
print("The Radius: ", area)

# Circumference 

def CircumferenceOfCircle(radius):
    pi = 3.1415926
    cir = 2 * pi * radius 
    return cir 

cir = CircumferenceOfCircle(radius)
print("The circumference: ", cir)

# Input function 
first_name = input("First name: ")
last_name = input("Last Name: ")
country = input("Country: ")
age = input("Age: ")

print(first_name, last_name, country, age)




