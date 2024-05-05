from client0 import Client
from Seq1 import *


# -- Parameters of your server
IP = "192.168.1.18"
PORT = 8080

c = Client(IP, PORT)


# -- Send a message to the server
s = Seq()
s.read_fasta("../sequences/FRAT1.txt")

count = 0
fragments = {'frag1': '' ,'frag2': '' ,'frag3': '','frag4': '','frag5': ''}
frag = ""
print(s)
for i in range(len(str(s))):
    frag += (str(s))[i]
    print(frag)
    if (i + 1) % 10 == 0:
        count += 1
        fragments[f'frag{count + 1}'] = frag
        frag = ""
print(fragments)

"""response1 = c.talk("Sending the U5 gene to the server...")
print("To Server: Sending the U5 gene to the server...")
print(f"From Server: {response1}")
response2 = c.talk(str(s))
print(f"To Server: {str(s)}")
print(f"From Server: {response2}")
"""