from client0 import Client


# -- Parameters of your server
IP = "212.128.255.76"
PORT = 8081

c = Client(IP, PORT)
# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")

