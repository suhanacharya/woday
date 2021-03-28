from bs4 import BeautifulSoup
import requests
import re
import datetime

word_pattern = r'\S+'

def get_wod_oed_link(source):
    print("Getting wod link from oed...")
    main_page = requests.get(source)
    soup = BeautifulSoup(main_page.content, 'html.parser')

    k = soup.find_all('p', class_="word")
    link = source[:-1] + k[0].find_all('a')[0]['href']

    return link

def get_wod_oed(source):
    link = get_wod_oed_link(source)

    main_page = requests.get(link)
    soup = BeautifulSoup(main_page.content, 'html.parser')

    word = soup.find_all('span', class_="hw")
    definition = soup.find_all('p', class_="entry-header")

    word = " ".join(re.findall(word_pattern, word[0].text))
    definition = " ".join(re.findall(word_pattern, definition[0].text))
    current_date = datetime.datetime.now()

    d = {
        "source": "OED",
        "date": str(current_date),
        "link": link, 
        "word": word,
        "definition": definition
    }

    return d