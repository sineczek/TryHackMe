import socket

HOST = "10.10.255.14"
PORT = 4000
host_HP = (HOST, PORT)
buffer_size=4096

#create socket to host
print("Connecting to "+HOST+" port "+str(PORT)+" ...")

#connect to host 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((host_HP))

#send ready to host
request = b'ready'
client.send(request)

#get response and assign value to variable
response = client.recv(buffer_size)
response = response.split(b' ')
key = response[0].split(b':')[1]
iv = response[1].split(b':')[1]
checksum = response[14]
print("Key:", key)
print("IV:", iv)
print("Checksum:", checksum)
