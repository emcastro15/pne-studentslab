#exercise 1
def seq_ping():
    print("OK")


#exercise 2

#exercise 3
def seq_len(seq):
    sequence = ""
    with open(seq, "r") as f:
        header = next(f)
        for line in f:
            sequence += line.strip("\n")
    return len(sequence)
