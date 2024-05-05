from client0 import Client


IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

print(c.talk("PING"))

for i in range(5):
    msg = f"GET {i}"
    print(c.talk(msg))

msg = f"INFO {c.talk('GET 0')}"
print(c.talk(msg))

msg = f"COMP {c.talk('GET 0')}"
print(c.talk(msg))

msg = f"REV {c.talk('GET 0')}"
print(c.talk(msg))

msg = f"GENE {c.talk('GET 0')}"
print(c.talk(msg))
