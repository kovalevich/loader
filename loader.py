import hashlib
from os import path
import requests
from bs4 import BeautifulSoup

CACHE_DIR = 'cache'


class Loader(object):

    def __init__(self):
        pass

    @classmethod
    def load(cls, url, cache=True) -> BeautifulSoup:
        file_name = CACHE_DIR + '/' + hashlib.md5(str(url).encode()).hexdigest()

        if cache and cls.__check(file_name):
            content = cls.__get(file_name)
        else:
            content = cls.__request(url)
            if cache and content:
                cls.__save(content, file_name)

        return BeautifulSoup(str(content), "html.parser")

    @classmethod
    def __save(cls, data, file):
        with open(file, 'w') as f:
            f.write(data)

    @classmethod
    def __get(cls, file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        if content:
            print(f'File {file} is read from cache')

        return content or None

    @classmethod
    def __check(cls, file):
        return path.exists(file)

    @classmethod
    def __request(cls, url):
        r = requests.get(url)
        if r.ok:
            print(f'Page {url} is downloaded!')
            return r.text
        else:
            print(f'Error download page: {url}')
            return False
