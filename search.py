#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import cgi

form = cgi.FieldStorage()
query = form.getvalue("q")

url = "https://www.google.com/maps/search/" + query
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
results = soup.find_all("div", {"class": ["section-result-content", "section-result-text-content"]})

output = ""
for result in results:
    name = result.find("h3", {"class": "section-result-title"}).text.strip()
    address = result.find("span", {"class": "section-result-location"}).text.strip()
    try:
        phone = result.find("span", {"class": "section-result-phone-number"}).text.strip()
    except AttributeError:
        phone = ""
    output += name + "<br>" + address + "<br>" + phone + "<br><br>"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print(output)
print("</body>")
print("</html>")
