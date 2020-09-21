import base64
import hashlib
import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
            Cipher, algorithms, modes
            )

def main():
    HOST = "10.10.255.14"
    PORT = 4000
    host_HP = (HOST, PORT)
    buffer_size = 4096
    
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
    hash_checksum = base64.b16encode(checksum).lower()
    print("Hash's Checksum:", hash_checksum)

    #request many time because tag may corrupt
    request = b'final'
    while 1:
        client.send(request)
        response = client.recv(buffer_size)
        ciphertext = response
        
        client.send(request)
        response = client.recv(buffer_size)
        tag = response
        
        try: 
            flag = do_decrypt(key, iv, ciphertext, tag).decode()
        except:
            flag = "no flag"
        
        hash_flag = get_hash(flag.encode())
        if hash_flag == hash_checksum:
            print("Hash's Flag:", hash_flag)
            print("Flag:", flag)
            break

def do_decrypt(key, iv, ciphertext, tag):
    decryptor = Cipher(algorithms.AES(key),
                modes.GCM(iv, tag),
                backend=default_backend()
                ).decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def get_hash(text): 
    hash_object = hashlib.sha256(text)
    hex_dig = hash_object.hexdigest()
    return hex_dig.encode()
main()
