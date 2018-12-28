from bs4 import BeautifulSoup
from requests import get


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
    r = get(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0"
        },
    )
    soup = BeautifulSoup(r.text, "lxml")
    return soup.find("link", href=True, attrs={"rel": "image_src"})["href"]
