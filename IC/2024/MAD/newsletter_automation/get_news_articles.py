from bs4 import BeautifulSoup
import requests
import urllib3
import pandas as pd


# convince site I'm a human
urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' + 
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

def reduce_lede(s, limit):
    return (s[:limit] + " ...") if limit < len(s) else s

def get_news_articles(file):
    # get url from file
    urls = pd.read_table(file, header=None)
    url = urls[0].iloc[0]
    # grab the HTML
    html = requests.get(url, headers=headers)

    # make sure it worked
    if html.status_code != 200:
        print(f'Request failed with status code: {html.status_code}')
    
    #parse html
    soup = BeautifulSoup(html.text, 'html.parser')
    image = soup.find("figure", class_="post-thumbnail").find('img')['src']

    title = str(soup.find("h1", class_="entry-title").text)

    lede = str(soup.find("div", class_="entry-content").find("p").text)

    max_chars = 180
    
    short_lede = reduce_lede(lede, max_chars)
    
    all_elements = {'image': image, 'title': title, 'lede': short_lede, 'url': url}
    output = pd.DataFrame(data=all_elements, index=[0])
    output.to_csv('test.csv')

if __name__=="__main__":
    get_news_articles("urls.txt")