from Seq1 import Seq


s = Seq()
s.read_fasta("../sequences/U5.txt")

print(f"Sequence 1: (Length: {s.len()}) {s}")
print(f"Bases: {s.count()}")
print(f"Reverse: {s.reverse()}")
print(f"Complement: {s.complement()}")

