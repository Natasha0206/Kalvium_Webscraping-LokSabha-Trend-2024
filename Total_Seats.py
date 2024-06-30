import requests
from bs4 import BeautifulSoup
req = requests.get("https://results.eci.gov.in/")
soup = BeautifulSoup(req.content,"html.parser")
res = soup.get_text()
print(res)

