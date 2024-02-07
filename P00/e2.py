# Implement the seq_read_fasta(filename) function.
# It should open a file in FASTA format and return a String with the DNA sequence.
# The header is removed as well as the '\n' characters.

from pathlib import Path


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    index = file_contents.find("\n")
    file_contents = (file_contents[index:]).replace("\n", "")
    result = f"""DNA file: U5.txt
    The first 20 bases are:
    {file_contents[1:21]}"""
    return result

FOLDER = "../sequences/"
FILENAME = "U5.txt"
filename = FOLDER + FILENAME
seq_read_fasta(filename)
