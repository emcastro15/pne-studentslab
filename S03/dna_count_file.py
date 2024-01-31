with open("dna.txt", "r") as f:
    count_dict = {}
    count_total = 0
    for line in f:
        count_total += len(line)
        for i in line:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count_dict[i] += 1
print(f"""Total length: {count_total}
A: {count_dict["A"]}
C: {count_dict["C"]}
G: {count_dict["G"]}
T: {count_dict["T"]}""")



