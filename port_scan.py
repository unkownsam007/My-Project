import argparse
import socket
import threading


def port_scan(tgt_host, tgt_ports):
    try:
        tgt_ip = socket.gethostbyname(tgt_host)   #this func resolve the ip from hostname and it ip then nothing just same
    except socket.herror:   #function prints the message corresponding to the error number contained in h_errno to stderr
        print(f'[-] Cannot resolve {tgt_host}: Unknown host')  #
        return 

    try:
        tgt_name = socket.gethostbyaddr(tgt_ip)     #resove hostname
        print(f'\n[+] Scan Results for: {tgt_name[0]}') #it may happen that there may be more than 1 ip's
    except socket.herror:
        print(f'\n[+] Scan Results for: {tgt_ip}')

    socket.setdefaulttimeout(1)

    for ports in tgt_ports:
        t = threading.Thread(target=conn_scan, args=(tgt_host, int(ports)))  
        t.start()


def conn_scan(tgt_host, tgt_port):
    screen_lock = threading.Semaphore() #Semaphore is simply an integer variable that is shared between threads     
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn_skt:
        try:
            conn_skt.connect((tgt_host, tgt_port))
            conn_skt.send(b'Cyber\r\n')   #pcan show by hosting a python web server
            results = conn_skt.recv(100).decode('utf-8') # 100 words grepping made by the request
            screen_lock.acquire() #lock and excecute until it is done
            print(f'[+] {tgt_port}/tcp open')
            print(f'   [>] {results}')
        except OSError:
            screen_lock.acquire()
            print(f'[-] {tgt_port}/tcp closed')
        finally:
            screen_lock.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='port_scan.py TARGET_HOST -p TARGET_PORTS'
              '\nexample: python3 port_scan.py scanme.nmap.org -p 21,80')

    parser.add_argument('tgt_host', type=str, metavar='TARGET_HOST',
                        help='specify target host (IP address or domain name)')
    parser.add_argument('-p', required=True, type=str, metavar='TARGET_PORTS',
                        help='specify target port[s] separated by comma '
                             '(no spaces)')
    args = parser.parse_args()  #take the arguments you provide on the command line when you run your program and interpret them according to the arguments you have added to your ArgumentParser object

    args.tgt_ports = str(args.p).split(',') #it converts into list 
    port_scan(args.tgt_host, args.tgt_ports)

