from client0 import Client
from seq1


# -- Parameters of your server
IP = "212.128.255.76"
PORT = 8081

c = Client(IP, PORT)


# -- Send a message to the server
s1 = Seq()
s1.read_fasta("../sequences/U5.txt")

print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")

