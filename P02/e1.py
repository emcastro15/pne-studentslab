from client0 import Client


# -- Parameters of your server
IP = "212.128.255.76"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.ping()
