import termcolor
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


def print_seqs(seq_list, color):
    for index, seq in enumerate(seq_list):
        seq_str = str(seq)
        termcolor.cprint(f"Sequence {index}: (Length: {len(seq_str)}) {seq}", color)


def generate_seqs(pattern, number):
    seq = ""
    seq_list = []
    for i in range(number):
        seq += pattern
        seq_list.append(seq)
    return seq_list


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, "blue")

print()
termcolor.cprint("List 2:", "yellow")
print_seqs(seq_list2, "yellow")
