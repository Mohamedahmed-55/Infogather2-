import requests
from bs4 import BeautifulSoup
def parse(url):
    print(f"Fetching {url}...")
    try:
        response=requests.get(url)
        soup=BeautifulSoup(response.text,"html.parser")
        title=soup.title.string if soup.title else "no title found"
        print(f"page title: {title}")
    except Exception as  e:
        print(f"failed to parse page: {e}")