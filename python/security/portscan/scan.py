import sys
import socket
import random
import time

def connect(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        s.connect((address, port))
        print ('[Warning]    ', address, 'is REACHABLE at', \
               str(port), 'port.')
    except Exception as e:
        print ('[Ok!]        ', address, 'is UNREACHABLE at', \
               str(port), 'port.')
    finally:
        s.close()



def main():
    if len(sys.argv) == 2:
        address = sys.argv[1]
        rand = 0
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        rand = random.randrange(0, int(sys.argv[2]), 1)
    else:
        print('Usage:', sys.argv[0], '<ip address> [random time (s)]', \
              file=sys.stderr)
        sys.exit(-1)

    #### Special ports to test:
    ports = [21, 22, 23, 80, 110, 115, 123, 161, 389, 443, 445, 465, \
             993, 1241, 1433, 1521, 3306, 3389, 5432, 9418]  
    
    for port in ports:
        connect(address, port) 
        time.sleep(rand)
    
    sys.exit(0)

if __name__=="__main__":
    main()
