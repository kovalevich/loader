import hashlib
from os import path
import requests


class Loader(object):

    CACHE_DIR = 'cache'

    def __init__(self):
        pass

    def load(self, url, cache=True):
        file_name = self.CACHE_DIR + '/' + hashlib.md5(str(url).encode()).hexdigest()

        if cache and self.__check(file_name):
            content = self.__get(file_name)
        else:
            content = self.__request(url)
            if cache and content:
                self.__save(content, file_name)
        return content

    def __save(self, data, file):
        with open(file, 'w') as f:
            f.write(data)

    def __get(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        if content:
            print(f'File {file} is read from cache')

        return content or None

    def __check(self, file):
        return path.exists(file)

    def __request(self, url):
        r = requests.get(url)
        if r.ok:
            print(f'Page {url} is downloaded!')
            return r.text
        else:
            print(f'Error download page: {url}')
            return False
