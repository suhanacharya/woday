from bs4 import BeautifulSoup
import requests
import re

word_pattern = r'\S+'


def get_wod_oed_link(source):
    # print("Getting wod link from oed...")
    main_page = requests.get(source)
    soup = BeautifulSoup(main_page.content, 'html.parser')

    k = soup.find_all('p', class_="word")
    link = source[:-1] + k[0].find_all('a')[0]['href']

    return link


def get_wod_oed(source):
    link = get_wod_oed_link(source)

    # print("Getting oed word definition...")
    main_page = requests.get(link)
    soup = BeautifulSoup(main_page.content, 'html.parser')

    word = soup.find_all('span', class_="hw")
    definition = soup.find_all('p', class_="entry-header")

    word = " ".join(re.findall(word_pattern, word[0].text))
    definition = " ".join(re.findall(word_pattern, definition[0].text))

    d = {
        "source": "OED",
        "link": link,
        "word": word,
        "definition": definition
    }

    # print("Gathered WOD from OED: success")

    return d


def get_wod_mw(source):
    # print('Getting wod from mw...')
    main_page = requests.get(source)
    soup = BeautifulSoup(main_page.content, 'html.parser')

    word = soup.find_all('h1')[0].text

    link = 'https://www.merriam-webster.com/dictionary/' + word
    # print(word)
    # print(link)

    # print("Getting mw definition of WOD...")

    word_page = requests.get(link)
    soup = BeautifulSoup(word_page.content, 'html.parser')

    definition = soup.find_all('div', class_="vg")
    word_pattern_sen = r'\S+'

    # definition = re.findall(word_pattern_sen, definition[0].text)
    definition = " ".join(re.findall(word_pattern_sen, definition[0].text))
    definition = re.findall(r'\D+', definition)
    definition = [x.strip() for x in definition]

    d = {
        "source": "MW",
        "link": link,
        "word": word,
        "definition": definition
    }

    # print("Gathered WOD from MW: success")

    return d


def get_wod_dict(source):
    # print('Getting wod from dictionary.com...')

    main_page = requests.get(source)
    soup = BeautifulSoup(main_page.content, 'html.parser')

    word = soup.find_all('div', class_="otd-item-headword__word")[0].text
    word = " ".join(re.findall(word_pattern, word))

    # print("Getting dictionary.com word definition...")
    definition = soup.find_all('div', class_="otd-item-headword__pos")[0]
    definition = definition.contents[-2].text

    # print(definition)

    d = {
        "source": "Dictionary.com",
        "link": source,
        "word": word,
        "definition": definition
    }

    # print("Gathered WOD from dictionary.com: success")

    return d
