class Seq:
    def __init__(self, strbases):
        if strbases.count("A") + strbases.count("C") + strbases.count("G") + strbases.count("T") == len(strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR!!!"
            print("INCORRECT Sequence detected")

    def __str__(self):
        return self.strbases

    def print_seqs(self, seq_list):
        for seq in seq_list:
            seq_index = index(seq)
            length = len(seq)

            return len(self.strbases),

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")