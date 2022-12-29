###PORT SCANNER#
###BY 0NKS0#

import socket

def scan():
    while True:
        try:
            s = socket.socket()
            PORT = input('Add Port to scan: [21/22/23]/Exit:  ')
            if 'exit' in PORT.lower():
                print('Closing Scanner')
                break
            else:
                s.connect(("{}".format(IP), int(PORT)))
                s.send(".".encode())
                s.settimeout(4)
                ret = s.recv(1024).decode()
                print("[+] The service is: " + ret + " And port: ", PORT)
                s.close()
        except Exception as err:
                print('[-] Port {} is closed\nThere was a connection error!\nMake sure there is a connection!'.format(PORT))
                print(err)
        print('Scan Finished Successfully!')

if __name__ == '__main__':
    print('Welcome to Port Scanner')
    IP = input('Please Add IP to scan: ')
    scan()
