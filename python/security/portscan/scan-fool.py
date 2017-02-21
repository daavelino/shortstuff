import sys
import socket

def connect(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        s.connect((address, port))
        print ("[Warning]        ", address, " is OPEN at ", str(port), " port.")
    except Exception as e:
        print ("[Ok!]        ", address, " is UNREACHABLE at ", str(port), " port.")
    finally:
        s.close()

def main():
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<ip address>', file=sys.stderr)
        sys.exit(-1)
  
    address = sys.argv[1]
    port_limit=65535
    for port in list(range(1, port_limit)):
        connect(address, port) 
    sys.exit(0)

if __name__=="__main__":
    main()
