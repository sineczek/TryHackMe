import socket

HOST = "10.10.255.14"
PORT = 4000
host_HP = (HOST, PORT)
buffer_size=4096

#create socket to host
print("Connecting to "+HOST+" port "+str(PORT)+" ...")
#send to host by using created UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((host_HP))
	
#send request to host
request = b'hello'
client.send(request)

#receive response
response = client.recv(buffer_size)
print(response)
