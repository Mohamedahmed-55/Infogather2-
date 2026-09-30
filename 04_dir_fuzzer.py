import requests


def dir_fuzzer(url):
    wordlist=["admin","images","gaming","vidues","films"]
    print(f"Starting Directory fuzzer on {url}")
    for word in wordlist:
        test_url=f"{url.rstrip('/')}/{word}"
        try:
            response=requests.get(test_url)
            if response.status_code==200:
                print(f"FOUND {test_url}")
        except requests.RequestException:
             print(f" Error accessing: {test_url}")
