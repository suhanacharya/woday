from bs4 import BeautifulSoup
import requests
from helper import get_wod_oed
import datetime

sources = ["https://www.oed.com/", "https://www.merriam-webster.com/word-of-the-day", "https://www.dictionary.com/e/word-of-the-day/", "https://www.thesaurus.com/e/synonym-of-the-day/"]

word_list = []

# get oed word
word_list.append(get_wod_oed(sources[0]))
print(word_list)


# soup = BeautifulSoup(main_page.content, 'html.parser')
# temp = open("temp.html",'w')
# temp.write(soup.prettify())