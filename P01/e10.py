from Seq1 import Seq


def most_frequent_base(counted_bases):
    print(counted_bases)
    highest_numb = 0
    highest_base = ""
    for base, number in counted_bases.items():
        if int(number) > highest_numb:
            highest_numb = int(number)
            highest_base = base
    return highest_base


s1 = Seq()
s1.read_fasta("../sequences/U5.txt")
print(f"Gene U5: Most frequent base: {most_frequent_base(s1.count())}")

s2 = Seq()
s2.read_fasta("../sequences/ADA.txt")
print(f"Gene ADA: Most frequent base: {most_frequent_base(s2.count())}")

s3 = Seq()
s3.read_fasta("../sequences/FRAT1.txt")
print(f"Gene FRAT1: Most frequent base: {most_frequent_base(s3.count())}")

s4 = Seq()
s4.read_fasta("../sequences/FXN.txt")
print(f"Gene FXN: Most frequent base: {most_frequent_base(s4.count())}")

s5 = Seq()
s5.read_fasta("../sequences/RNU6_269P.txt")
print(f"Gene RNU6_269P: Most frequent base: {most_frequent_base(s5.count())}")
