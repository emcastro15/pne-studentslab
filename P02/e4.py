from client0 import Client
from Seq1 import *


# -- Parameters of your server
IP = "192.168.1.18"
PORT = 8080

c = Client(IP, PORT)


# -- Send a message to the server
s = Seq()
s.read_fasta("../sequences/U5.txt")

response1 = c.talk("Sending the U5 gene to the server...")
print("To Server: Sending the U5 gene to the server...")
print(f"From Server: {response1}")
response2 = c.talk(str(s))
print(f"To Server: {str(s)}")
print(f"From Server: {response2}")
