import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the website to scrape
URL="https://simpleflying.com/"

# Define custom headers to mimic a browser request
HEADER={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" ,
    "Accept-Language": "en-US,en;q=0.9"}

# Send a GET request to the URL with the custom headers
response=requests.get(URL, headers=HEADER)
html_content=response.text

#Create a BeautifulSoup object to parse the HTML content
soup=BeautifulSoup(html_content, "html.parser")

# Find all article titles on the page
article=soup.find_all("h3", class_="display-card-title")

#print(article)


url_sn="https://spacenews.com/"
response_sn=requests.get(url_sn, headers=HEADER)
soup_sn=BeautifulSoup(response_sn.text, "html.parser")
sn_data=[]
articles_sn=soup_sn.find_all(["h3","h2"], class_=lambda x: x and "title" in x)
print(articles_sn)