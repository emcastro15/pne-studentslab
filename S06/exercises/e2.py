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


def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        seq_str = str(seq)
        print(f"Sequence {index}: (Length: {len(seq_str)}) {seq}")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)
