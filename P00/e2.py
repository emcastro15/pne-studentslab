# Implement the seq_read_fasta(filename) function.
# It should open a file in FASTA format and return a String with the DNA sequence.
# The header is removed as well as the '\n' characters.

from seq0 import *
filename = '../sequences/U5_sequence.fa'
sequence = seq_read_fasta(filename)
print("DNA sequence:")
print(sequence)
