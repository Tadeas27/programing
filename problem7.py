def swap(a, b):
    # Write your code here to swap the values of a and b
    c = a
    a = b
    b = c
    return a,b

# Example usage:
a = 5
b = 10
print("Before swap: a =", a, "b =", b)

a, b = swap(a, b)

print("After swap: a =", a, "b =", b)