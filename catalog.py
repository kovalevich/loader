from loader import Loader
from db import Db

DATABASE = 'auto'
DB_USER = 'kavalevich'
DB_PASS = '1'


if __name__ == '__main__':

    soup = Loader.load('https://cars.av.by/')
    db = Db(DATABASE, DB_USER, DB_PASS)

    q = 'delete from marka; delete from models;'
    db.sql(q)

    categories = soup.findAll('a', class_='catalog__link')

    for category in categories:

        name = category.contents[0].text

        q = f'insert into marka (name) values (%s) RETURNING id'
        id = db.fetch_one(q, db.clear(name))

        url = 'https://cars.av.by' + category.attrs['href']
        s = Loader.load(url)

        models = s.findAll('a', class_='catalog__link')

        for model in models:

            model_name = model.contents[0].text
            q = f'insert into models (name, marka_id) values (%s, %s)'
            db.sql(q, model_name, str(id))
            print(f'{name} {model_name}')
