import requests
from bs4 import BeautifulSoup
req = requests.get("https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S28.htm")
soup = BeautifulSoup(req.content,"html.parser")
res = soup.get_text()
text = " ".join(res.split())

temp = ""
for i in text:
    if (i.isspace() or i.isalnum()==False):
        print(temp)
        temp = ""
        continue
    else:
        temp+=i