age = 22
height = 180.34
imaginary = 3+ 4j

base = float(input("Enter base: "))
height = float(input("Enter height: "))

def AreaOfTriangle(base, height):
    AreaTriangle = 0.5 * base * height
    return AreaTriangle

area = AreaOfTriangle(base, height)
print(area)

# Step 5
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

print(a+b+c)