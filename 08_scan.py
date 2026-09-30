import socket
def port_scanner(host):
    print(f"scaning {host}")
    for port in range(20,1025):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        result=s.connect_ex((host,port))
        if result==0:
            print(f"the port {port} on {host} is open")
            s.close()
            
            
