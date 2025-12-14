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
if not article:
    articles=soup.find_all("article")

news_data=[]

# Extract headlines and links from the articles
for item in article:
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
                "source": "simpleflying",
                "Headline": headline,
                "Link": link
            })



# Now scrape SpaceNews
url_sn="https://spacenews.com/"
response_sn=requests.get(url_sn, headers=HEADER)
soup_sn=BeautifulSoup(response_sn.text, "html.parser")
sn_data=[]
articles_sn=soup_sn.find_all(["h3","h2"], class_=lambda x: x and "title" in x)
for item in articles_sn:
    link_tag=item.find("a")
    if link_tag:
        headline=link_tag.get_text(strip=True)
        link=link_tag['href']

        if headline:
            sn_data.append({
                "source": "spacenews",
                "Headline": headline,
                "Link": link
            })




# Combine data from both sources
df1=pd.DataFrame(news_data)
df2=pd.DataFrame(sn_data)

combined_df=pd.concat([df1, df2], ignore_index=True)
combined_df.to_csv("aerospace_news.csv", index=False)

print(f"Scraped {len(combined_df)} articles and saved to aerospace_news.csv")
print("saved to aerospace_news.csv")
print(combined_df.head(20))