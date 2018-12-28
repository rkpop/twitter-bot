from bs4 import BeautifulSoup
from requests import get
from kpopbot import HEADER


def media_provider(url):
    if "i.redd.it" in url:
        return url
    elif "imgur.com/a/" in url:
        return first_image(url)
    elif "i.imgur.com" in url:
        return url
    else:
        return None


def first_image(url):
    r = get(url, headers=HEADER)
    soup = BeautifulSoup(r.text, "lxml")
    return soup.find("link", href=True, attrs={"rel": "image_src"})["href"]
