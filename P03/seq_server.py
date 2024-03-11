import socket

PORT = 8080
IP = "127.0.0.1" # this IP address is local, so only requests from the same machine are possible

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((IP, PORT))

ls.listen()

print("The server is configured!")

ls.close()


PORT = 8080
IP = "127.0.0.1" # the IP address depends on the machine running the server

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((IP, PORT))

ls.listen()

print("The server is configured!")

print("A client has connected to the server!")

while True:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        if msg.startswith('PING'):
            print("PING command")
            response = "OK!\n"
            cs.send(response.encode())
        elif msg.startswith('GET'):
            print("GET command")
            response = "OK!"
            cs.send(response.encode())
        cs.close()

#you can also do this with the code of techers server, try to understand both (techers is easier)