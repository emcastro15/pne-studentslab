# --- Find the error!


def g(a, b):
    return a - b


def f(a, b, c, d):
    t0 = a + b - g(a, 0)
    t1 = g(c, d)
    t3 = 2 * (t0 / t1)  #The error happens because there can be a possible zero division we can fix this by making an exception for xerodivision
    return t0 + (2 * t1) + (t3 * t3)


# -- Main program
print("Result 1: ", f(5, 2, 5, 0))
print("Result 2: ", f(0, 2, 3, 3))
print("Result 3: ", f(1, 3, 2, 3))
print("Result 4: ", f(1, 9, 22.0, 3))