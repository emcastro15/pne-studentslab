from client0 import Client


IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

msg = "GENE U5"

print(c.talk(msg))