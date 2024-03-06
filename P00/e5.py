from Seq0 import *
filename = ['../sequences/U5.txt', '../sequences/ADA.txt','../sequences/FRAT1.txt','../sequences/FXN.txt','../sequences/RNU6_269P.txt']
final_name_list = ['Gene U5:','Gene ADA:','Gene FRAT1:','Gene FXN:','Gene RNU6_269P:']

for i in filename:
    num = filename.index(i)
    print(final_name_list[num], seq_count(i))