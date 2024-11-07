def multiply_point():
    # Taking user input for the elliptic curve parameters
    print("Equation is of the form: y^2 = x^3 + ax + b mod p")
    a = int(input("Enter the value of 'a': "))
    b = int(input("Enter the value of 'b': "))
    p = int(input("Enter the prime 'p' for the finite field: "))
    
    # Taking user input for the point and multiplier
    x1 = int(input("Enter the x-coordinate of point P: "))
    y1 = int(input("Enter the y-coordinate of point P: "))
    n = int(input("Enter the scalar multiplier 'n' for nP: "))
    
    # Helper function to perform modular inverse
    def mod_inv(x, p):
        return pow(x, p - 2, p)
    
    # Initializing the result to the input point (x1, y1)
    result_x, result_y = x1, y1
    
    # Point multiplication loop
    for _ in range(n - 1):
        # Slope calculation for addition or doubling
        if result_x == x1 and result_y == y1:
            # Point doubling
            slope = (3 * result_x**2 + a) * mod_inv(2 * result_y, p) % p
        else:
            # Point addition
            slope = (y1 - result_y) * mod_inv(x1 - result_x, p) % p

        # Calculate the resulting point R = P + Q
        new_x = (slope**2 - result_x - x1) % p
        new_y = (slope * (result_x - new_x) - result_y) % p
        result_x, result_y = new_x, new_y

    # Output the result
    print(f"{n}P =", (result_x, result_y))