# Function to perform modular inverse
def mod_inv(x, p):
    return pow(x, p - 2, p)

# Function to add two points P and Q
def add_points(x1, y1, x2, y2, a, p):
    #slope calculation
    if x1 == x2 and y1 == y2:
        # Point doubling
        slope = (3 * x1**2 + a) * mod_inv(2 * y1, p) % p
    else:
        # Point addition
        slope = (y2 - y1) * mod_inv(x2 - x1, p) % p
    
    # Calculate the resulting point R = P + Q
    x_r = (slope**2 - x1 - x2) % p
    y_r = (slope * (x1 - x_r) - y1) % p
    
    return (x_r, y_r)

# Function to multiply a point by number n
def multiply_point(n, x1, y1, a, p):
    result_x, result_y = x1, y1
    for _ in range(n - 1):
        result_x, result_y = add_points(result_x, result_y, x1, y1, a, p)
    return (result_x, result_y)

print("Equation is of the form: y^2=x^2+ax+b mod p")

# Taking user input
a = int(input("Enter the value of 'a': "))
b = int(input("Enter the value of 'b': "))
p = int(input("Enter 'p' for the finite field: "))

x1 = int(input("Enter x-coordinate of point P: "))
y1 = int(input("Enter y-coordinate of point P: "))
x2 = int(input("Enter x-coordinate of point Q: "))
y2 = int(input("Enter y-coordinate of point Q: "))

x_r, y_r = add_points(x1, y1, x2, y2, a, p)
print("P + Q =", (x_r, y_r))

# Taking user input
n = int(input("Enter the number n to multiply the point P (nP): "))
nP = multiply_point(n, x_r, y_r, a, p)
print(f"{n}P =", nP)