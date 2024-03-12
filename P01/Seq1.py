import termcolor


class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence created!")
        elif strbases.count("A") + strbases.count("C") + strbases.count("G") + strbases.count("T") == len(strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR!"
            print("INVALID sequence!")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR!":
            length = 0
        else:
            length = len(self.strbases)
        return length

    def count_base(self, base):
        count = 0
        if self.strbases == "NULL" or self.strbases == "ERROR!":
            pass
        else:
            for i in self.strbases:
                if i == base:
                    count += 1
        return count

    def count(self):
        count_bases = {}
        if self.strbases == "NULL" or self.strbases == "ERROR!":
            for base in "ACTG":
                count_bases[base] = 0
        else:
            for base in self.strbases:
                if base not in count_bases:
                    count_bases[base] = 1
                else:
                    count_bases[base] += 1
        return count_bases

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR!":
            rev = self.strbases
        else:
            rev = self.strbases[::-1]
        return rev

    def complement(self):
        complements_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        comp = ""
        if self.strbases == "NULL" or self.strbases == "ERROR!":
            comp = self.strbases
        else:
            for base in self.strbases:
                comp += complements_dict[base]
        return comp

    def read_fasta(self, filename):
        sequence = ""
        with open(filename, "r") as f:
            header = next(f).replace("\n", "")
            for line in f:
                sequence = line.replace("\n", "")
        self.strbases = sequence
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


