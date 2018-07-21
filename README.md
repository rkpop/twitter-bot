# /r/kpop Twitter bot

A bot to tweet link to posts on /r/kpop that has 100 points or more.

## Requirements

* Python 3.6+

* PRAW

* [twitter](https://github.com/sixohsix/twitter)

* Virtualenv

* Valid Twitter and Reddit API keys

## Installation

* git pull

* Create new virtualenv

* Open a new env terminal

* `pip3 install -r requirements.txt`

## Configuration

Copy `CONFIG.py.sample` as `CONFIG.py` and fill out with the keys obtained from Twitter API and Reddit API.

## Running the script

Ensure that the configuration is done correctly, then do `python3 __main__.py` on the env terminal.

## TODO

* Proper exception handling

* Image upload for image posts