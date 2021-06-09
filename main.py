# from deta import App
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
import json
# import datetime
from helper import get_wod_oed, get_wod_mw, get_wod_dict

app = FastAPI()


sources = ["https://www.oed.com/", "https://www.merriam-webster.com/word-of-the-day",
           "https://www.dictionary.com/e/word-of-the-day/", "https://www.thesaurus.com/e/synonym-of-the-day/"]

# word_list = []
# word_list.append(get_wod_oed(sources[0]))
# word_list.append(get_wod_mw(sources[1]))
# word_list.append(get_wod_dict(sources[2]))
# print(word_list)


@app.get("/")
def hello():
    return {'response': 'hello welcome to woday'}


@app.get("/all")
def main():
    # word_dict = dict()
    # today = str(datetime.date.today())
    word_dict = []

    # print("Gathering resources...")

    # * get oed word
    word_dict.append(get_wod_oed(sources[0]))

    # * get merriam-webster wod
    word_dict.append(get_wod_mw(sources[1]))

    # * get dictionary.com wod
    word_dict.append(get_wod_dict(sources[2]))

    word_dict = jsonable_encoder(word_dict)
    return JSONResponse(content=word_dict)

    # return {'response': 'Server is now Ready'}

    # with open("wod.json", "a") as jfile:
    #     print(word_dict)
    #     json.dump(word_dict, jfile, indent=4)


if __name__ == "__main__":
    main()

# main_page = requests.get(sources[1])
# soup = BeautifulSoup(main_page.content, 'html.parser')
# temp = open("temp.html",'w')
# temp.write(soup.prettify())

# temp = open("temp.html")
# soup = BeautifulSoup(temp, 'html.parser')
# word = soup.find_all('h1')[0].text
# def_req = requests.get(sources[1] + 'dictionary/' + word)

# print(word)
