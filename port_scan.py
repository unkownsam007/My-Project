import socket
target = (input('Enter ip address e.g. 192.168.0.0:'))
port = (input('Enter Port Numnber e.g.80,443:'))
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False
print(portscan(port))