from client0 import Client


IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

for i in range(5):
    msg = f"GET {i}"
    print(c.talk(msg))