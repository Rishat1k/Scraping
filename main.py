import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


keywords = ['дизайн', 'фото', 'web', 'python']
headers_generator = Headers(os="win", browser="firefox")

response = requests.get('https://habr.com/ru/articles/', headers=headers_generator.generate())

html_data = response.text
soup = BeautifulSoup(html_data, 'lxml')
articles_list = soup.find(name='div', class_="tm-articles-list")
articles = articles_list.find_all('article')

for article_tag in articles:
    preview = article_tag.find(name='div', class_='article-formatted-body')
    preview_text = preview.text

    for word in keywords:
        if word in preview_text:
            time_tag = article_tag.find('time')
            date_time = time_tag['datetime']

            name_tag = article_tag.find(name='a', class_='tm-title__link')
            title = name_tag.find('span')
            title_text = title.text.strip()

            link_relative = name_tag["href"]
            link_absolute = f'https://habr.com{link_relative}'

            print(date_time, title_text, link_absolute)
            break


