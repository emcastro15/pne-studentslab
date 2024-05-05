from client0 import Client


# -- Parameters of your server
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

print(c.talk("PING"))