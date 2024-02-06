from pathlib import Path

FILENAME = "sequences/ADA.txt"

file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split("\n")
list_contents.pop(0)     #pop is used to remove the header
print(len(''.join(list_contents)))


#another option
index = file_contents.find("\n")
file_contents = (file_contents[index:]).replace("\n","")
print(len(file_contents))