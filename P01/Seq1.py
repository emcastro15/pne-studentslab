class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases=""):
        bases_list = ["A", "C", "G", "T"]
        flag = True
        for i in strbases:
            if i not in bases_list:
                self.strbases = "ERROR"
                flag = False
            break
        if strbases : ""

        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")
