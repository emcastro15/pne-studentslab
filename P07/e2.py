import termcolor
from genes_dict import genes

print("Dictionary of Genes!")
print(f"There are {len(genes)} genes in the dictionary:")
for key in genes.keys():
    termcolor.cprint(key, 'green', end="")
    print(f": --> {genes[key]}")

# or
"""for key, value in genes.items():
    termcolor.cprint(key, 'green', end="")
    print(f": --> {value}")"""