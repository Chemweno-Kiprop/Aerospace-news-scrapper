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
article=soup.find_all("a", class_="display-card-title")
if not article:
    articles=soup.find_all("article")

news_data=[]

for item in articles:
    link_element=None
    if item.name=='a':
        link_element=item
    else:
        link_element=item.find("a")

    if link_element:
        headline=link_element.get_text(strip=True)
        link=link_element['href']

        if link and not link.startswith("http"):
            link="https://simpleflying.com" + link

        if headline:
            news_data.append({
                "Headline": headline,
                "Link": link
            })

df=pd.DataFrame(news_data)

print("-- Latest News Articles --")

if not df.empty:
    print(df(10))
else:
    print("No articles found.")


