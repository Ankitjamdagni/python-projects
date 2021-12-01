import socket
import sys
from typing import Collection

def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port=9999
        s=socket.socket()
    except socket.error as msg:
        print("error while crating socket" + str(msg))
    
def bind_socket():
    try:
        global host
        global port
        global s
        print("sucessfuly bind with port" + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as mssg:
        print("error while binding socket" + str(mssg) + "and retrying")
        bind_socket()

def socket_accept():
    conn,add=s.accept()
    print("connection established with ip : " + add[0] + "and port is : " + str(add[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd=input("enter the command")
        if cmd=="quit":
            conn.close()
            s.close()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            clientresponce=str(conn.recv(1024),"utf-8")
            print(clientresponce,end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()