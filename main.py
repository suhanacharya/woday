from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from bs4 import BeautifulSoup
import requests

from helper import get_wod_oed, get_wod_mw, get_wod_dict


app = FastAPI()

sources = ["https://www.oed.com/", "https://www.merriam-webster.com/word-of-the-day",
           "https://www.dictionary.com/e/word-of-the-day/", "https://www.thesaurus.com/e/synonym-of-the-day/"]


@app.get("/")
def hello():
    return {'response': 'hello welcome to woday, to get started, checkout /docs endpoint'}


@app.get("/1")
def main():
    # * get oed word
    word_dict = get_wod_oed(sources[0])

    word_dict = jsonable_encoder(word_dict)
    return JSONResponse(content=word_dict)


@app.get("/2")
def main():
    # * get merriam-webster wod
    word_dict = get_wod_mw(sources[1])

    word_dict = jsonable_encoder(word_dict)
    return JSONResponse(content=word_dict)


@app.get("/3")
def main():
    # * get dictionary.com wod
    word_dict = get_wod_dict(sources[2])

    word_dict = jsonable_encoder(word_dict)
    return JSONResponse(content=word_dict)

# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         word1 = asyncio.ensure_future(get_wod_oed(session, sources[0]))
#         word2 = asyncio.ensure_future(get_wod_mw(session, sources[1]))
#         word3 = asyncio.ensure_future(get_wod_mw(session, sources[2]))

#         tasks = [word1, word2, word3]

#     words = await asyncio.gather(*tasks)

#     word_dict = jsonable_encoder(words)
#     return JSONResponse(content=word_dict)


# @app.get('/all')
# def get_all():
#     return asyncio.run(main())
