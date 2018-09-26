import requests
from bs4 import BeautifulSoup


class Parse:
    def __init__(self, url, name, password):
        """Иницилизируем session, проверяем успешно или нет"""
        self.session = requests.Session()
        values = {'auth_name': name,
                  'auth_pass': password}
        page = self.session.post(url, data=values)
        self.authorization = True if page.status_code == 200 else False

    def parse_finish(self, url):
        html = self.session.get(url).text
        soup = BeautifulSoup(html, features='lxml')
        answer = (soup.find('table', {'class': 'maintable', 'border': '0', 'width': '100%',
                                      'bgcolor': '#EBEBEB', 'cellspacing': '0', 'cellpadding': '4', })
                      .find_all('a', {'href': True})[2])
        return answer

    def parse_url(self, url):
        """Извлекаем признаки по заданному адресу"""
        html = self.session.get(url).text
        soup = BeautifulSoup(html, features='lxml')
        try:
            answer = (list(soup.find('font', {'size': '2'})) +
                      list(soup.find('tr', {'height': '20'})
                               .find_all('a', {'href': True})) +
                      list(soup.find('table', {'bgcolor': 'D0D0D0', 'border': '0',
                                               'cellpadding': '4', 'cellspacing': '1', 'width': '100%', })))
        except Exception:
            return []
        return answer
