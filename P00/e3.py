from Seq0 import *
list_seq = ["../sequences/ADA.txt", "../sequences/FRAT1.txt", "../sequences/FXN.txt", "../sequences/RNU6_269P.txt", "../sequences/U5.txt"]
list_name = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
for i in list_seq:
    for n in list_name:
        if n in i:
            leng = seq_len(i)
            print("Gene", n, "-> Length:", leng)