class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        # initialize a sequence with a value
        # passed as an argument when creating an object
        self.strbases = strbases
        print("New sequence created!")  # DO NOT PRINT HERE (just an exception)


# Main program
# Create an object of the class Seq
#s1 = Seq()
#s2 = Seq()
s1 = Seq("AGTACATGGT")
s2 = Seq("CGTAAC")
print("Testing...")
