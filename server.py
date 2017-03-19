#!/usr/bin/env python3
#encoding: UTF-8

from socket import *
import time


HOST = "127.0.0.1"
PORT = 4300
def readFile():
    d = {}
    file = open('geo_world.txt', 'r')
    for line in file:
        line = line.strip().split(' - ')
        d[line[0]] = line[1]
    return d

if __name__ == "__main__":
    print("Reading a file...")
    x = time.clock()
    d = readFile()
    print("Read in ", time.clock()-x, " seconds")
    server_sckt = socket(AF_INET, SOCK_DGRAM)
    server_sckt.bind((HOST, PORT))
    print("Listening on %s:%d" % (HOST, PORT))

    while True:
        
        (msg_req, client_addr) = server_sckt.recvfrom(2048)
        print("User query: ", msg_req.decode())
        
        if msg_req.decode() == 'BYE':
            server_sckt.sendto('BYE'.encode(), client_addr)
            break
        else:
            try:
                msg_resp = d[msg_req.decode()]
            except:
                msg_resp = "There is no such country"
        
        server_sckt.sendto(msg_resp.encode(), client_addr)
    print("Stopping the server")
    server_sckt.close()