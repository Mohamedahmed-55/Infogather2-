import os
def ping_target(target):
    print(f"pinging {target}")
    response=os.system(f"ping -n 4 {target}")
    if response==0:
        print("Host is reachable")
    else:
        print("Host is unreachable")