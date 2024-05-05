from client0 import Client


# -- Parameters of your server
IP = "192.168.1.18"
PORT = 8080

c = Client(IP, PORT)
# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")

