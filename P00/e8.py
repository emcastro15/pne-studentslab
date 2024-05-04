from Seq0 import *

filename = ['../sequences/U5.txt', '../sequences/ADA.txt','../sequences/FRAT1.txt','../sequences/FXN.txt','../sequences/RNU6_269P.txt']
final_name_list = ['Gene U5:','Gene ADA:','Gene FRAT1:','Gene FXN:','Gene RNU6_269P:']

gene_filename_dict = dict(zip(final_name_list, filename))

for key, value in gene_filename_dict.items():
    counted_bases = seq_count(value)
    print(f"{key}: Most frequent Base: {most_frequent_base(counted_bases)}")