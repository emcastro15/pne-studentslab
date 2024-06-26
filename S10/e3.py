import socket
from termcolor import colored

# Configure the Server's IP and PORT
PORT = 8081
IP = "212.128.254.250"  # the IP address depends on the machine running the server

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

number_connections = 0
list_clients = []

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")
        number_connections += 1
        list_clients.append(client_ip_port)

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-readable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"CONNECTION {number_connections}. Client IP,PORT: {client_ip_port}")
        print(f"Message received: {colored(msg, 'green')}")

        # -- Send a response message to the client
        response = f"ECHO: {msg}\n"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # loop to send message after 5 clients have connected
        if number_connections == 5:
            print("The following clients have connected to the server:")
            number_client = 0
            for client in list_clients:
                print(f"Client {number_client}: {client}")
                number_client += 1

        # -- Close the data socket
        cs.close()