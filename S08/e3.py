import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.1.18" # depends on the computer the server is running


while True:
  # -- Ask the user for the message
    user_input = input("Enter: ")
    if user_input == "Chatapp":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        s.send(str.encode("HELLO FROM THE CLIENT!!!"))
        s.close()

