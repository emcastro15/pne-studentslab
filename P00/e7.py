from Seq0 import *
print('Gene U5:')
seq = seq_reverse('../sequences/U5.txt', 6)
print('Fragment:', seq)
print('Complement:', seq_complement(seq))
