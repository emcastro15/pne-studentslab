import socket

# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.76" # depends on the computer the server is running


while True:
  # -- Ask the user for the message
    user_input = input("Enter: ")
    if user_input == "Chatapp":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        s.send(str.encode("HELLO FROM THE CLIENT!!!"))
        s.close()

