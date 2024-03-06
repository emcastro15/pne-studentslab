class Seq:
    """A class for representing sequences"""
    pass

# Main program
# Create an object of the class Seq
s1 = Seq()

# Create another object of the Class Seq
s2 = Seq()

class Seq:
    """A class for representing sequences"""
    def __init__(self):
        print("New sequence created!") # It's not good practice to print here but let's make an exception!


# Main program
# Create an object of the class Seq
s1 = Seq()
s2 = Seq()
print("Testing...")

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
print("Testing....")
