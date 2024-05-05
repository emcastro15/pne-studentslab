import socket
from Seq1 import *

sequences = ["ATCGATCGAT", "CGATCGATCG", "GATCGATCGA", "ATCGATCGTA", "TCGATCGATC"]
gene_files = {
    'U5': '../sequences/U5.txt',
    'ADA': '../sequences/ADA.txt',
    'FRAT1': '../sequences/FRAT1.txt',
    'FXN': '../sequences/FXN.txt',
    'RNU6_269P': '../sequences/RNU6_269P.txt'
}

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
            print(response)
        elif msg.startswith('GET'):
            print("GET command")
            num = int(msg.split(" ")[1])
            if 0 <= num <= 4:
                response = sequences[num]
            else:
                response = "Invalid number! Number should be between 0 and 4."
            cs.send(response.encode())
            print(response)
        elif msg.startswith('INFO'):
            print("INFO command")
            sequence = msg.split(" ")[1]
            s1 = Seq(sequence)
            bases_length = s1.len()
            bases_count = s1.count()
            response = f"Sequence: {sequence}\nTotal length: {bases_length}\n"
            for key, value in bases_count.items():
                percentage = round((value / bases_length) * 100, 1)
                response += f"{key}: {value} ({percentage}%)\n"
            cs.send(response.encode())
            print(response)
        elif msg.startswith('COMP'):
            print("COMP command")
            sequence = msg.split(" ")[1]
            s1 = Seq(sequence)
            response = s1.complement()
            cs.send(response.encode())
            print(response)
        elif msg.startswith('REV'):
            print("REV command")
            sequence = msg.split(" ")[1]
            s1 = Seq(sequence)
            response = s1.reverse()
            cs.send(response.encode())
            print(response)
        elif msg.startswith('GENE'):
            print("GENE command")
            gene_name = msg.split(" ")[1]
            if gene_name in gene_files:
                s1 = Seq()
                response = s1.read_fasta(gene_files[gene_name])
            else:
                response = f"Invalid gene name: {gene_name}"
            cs.send(response.encode())
            print(response)
        cs.close()

