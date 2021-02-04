from loader import Loader


if __name__ == '__main__':

    soup = Loader.load('https://cars.av.by/')

    categories = soup.findAll('a', class_='catalog__link')

    for category in categories:

        name = category.text
        url = 'https://cars.av.by' + category.attrs['href']
        s = Loader.load(url)

        models = s.findAll('a', class_='catalog__link')

        for model in models:

            print(f'{name} {model.text}')
