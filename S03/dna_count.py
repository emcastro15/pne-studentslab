#Introduce the sequence: CATGTAGACTAG
#Total length: 12
#A: 4
#C: 2
#T: 3
#G: 3

sequence_dna = input("Enter a valid DNA sequence: ").upper()
length_dna = len(sequence_dna)
count_a = sequence_dna.count("A")
count_g = sequence_dna.count("G")
count_c = sequence_dna.count("C")
count_t = sequence_dna.count("T")
print(length_dna)
print(f"""Total length: {length_dna}
A: {count_a}
C: {count_c}
G: {count_g}
T: {count_t}""")

#this can also be done with a dictionary

count_dict = {}
sequence_dna = input("Enter a valid DNA sequence: ").upper()
count_total = len(sequence_dna)
for i in sequence_dna:
    if i not in count_dict:
        count_dict[i] = 1
    else:
        count_dict[i] += 1
print(f"""Total length: {count_total}
A: {count_dict["A"]}
C: {count_dict["C"]}
G: {count_dict["G"]}
T: {count_dict["T"]}""")
