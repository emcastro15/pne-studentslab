#exercise 1
def seq_ping():
    print("OK")


#exercise 2
def seq_read_fasta(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            seq_joined = ''.join(lines[1:])
            sequence = seq_joined[:20]
    except FileNotFoundError:
        print("Error: File", filename, "not found.")
        sequence = None
    return sequence


#exercise 3
def seq_len(seq, list_seq, list_names):
    sequence = ""
    with open(seq, "r") as f:
        header = next(f)
        for line in f:
            sequence += line.strip("\n")
    return len(sequence)


#exercise 4
def seq_count_base(seq, base):
    try:
        with open(seq, 'r') as file:
            lines = file.readlines()
            seq_joined = ''.join(lines[1:])
    except FileNotFoundError:
        print("Error: File", seq, "not found.")
        count_base = None
    else:
        count_base = 0
        for i in seq_joined:
            if i == base.upper():
                count_base += 1
            else:
                pass
    return count_base


# exercise 5
def seq_count(seq):
    try:
        with open(seq, 'r') as file:
            lines = file.readlines()
            seq_joined = ''.join(lines[1:])
    except FileNotFoundError:
        print("Error: File", seq, "not found.")
        dic_bases = {}
    else:
        dic_bases = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
        for i in seq_joined:
            if i == 'A':
                dic_bases['A'] += 1
            elif i == 'T':
                dic_bases['T'] += 1
            elif i == 'C':
                dic_bases['C'] += 1
            elif i == 'G':
                dic_bases['G'] += 1
    return dic_bases


# exercise 6
def seq_reverse(seq, n):
    try:
        with open(seq, 'r') as file:
            lines = file.readlines()
            seq_joined = ''.join(lines[1:])
            sequence = seq_joined[:n]
    except FileNotFoundError:
        print("Error: File", seq, "not found.")
        sequence = None
    return sequence


# exercise 7
def seq_complement(seq):
    comp = ""
    for i in seq:
        if i == "A":
            comp += "T"
        elif i == "C":
            comp += "G"
        elif i == "G":
            comp += "C"
        elif i == "T":
            comp += "A"
    return comp


# exercise 8
def most_frequent_base(counted_bases):
    # print(counted_bases)
    highest_numb = 0
    highest_base = ""
    for base, number in counted_bases.items():
        if int(number) > highest_numb:
            highest_numb = int(number)
            highest_base = base
    return highest_base
