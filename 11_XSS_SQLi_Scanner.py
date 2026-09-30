import requests
def scan_vulnerabilities(url):
    print(f"Scaning for xss/sqli on: {url}")
    xss_payload="<script>alert ('XSS') </script>"
    sqli_payload="' OR '1'='1"
    try:
        r1=requests.get(f"{url}?q={xss_payload}")
        if xss_payload in r1.text:
            print("possible xss vulnerability found")

        r2=requests.get(f"{url}?id={sqli_payload}")
        if sqli_payload in r2.text:
            print("possible sqli vulnerability found")
    except Exception as e:
        print(f"error {e}")
