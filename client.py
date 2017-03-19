#!/usr/bin/env python3
#encoding: UTF-8

from socket import *

HOST = "127.0.0.1"
PORT = 4300

if __name__ == "__main__":
    client_sckt = socket(AF_INET, SOCK_DGRAM)
    
    while True:
        msg_req = input('Enter country or BYE to quit: ')
        client_sckt.sendto(msg_req.encode(), (HOST, PORT))
        (msg_resp, server_addr) = client_sckt.recvfrom(2048)
        print('\n', msg_resp.decode(), '\n')
        if msg_resp.decode() == "BYE":
            break
    print("Stopping the client")
    client_sckt.close()