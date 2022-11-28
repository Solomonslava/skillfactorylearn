import requests as re
from bs4 import BeautifulSoup

def main():
    base = 'https://ru.stackoverflow.com'
    html = re.get(base).content
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', id='question-mini-list')
    a = div.find_all('a', class_='s-link')
    for _ in a:
        if _.string:
            print(_.string, base + _['href'])

if __name__ == '__main__':
    main()