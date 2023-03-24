import requests
from bs4 import BeautifulSoup

class News:
    def __init__(self,title, annotaion, full_text, link):
        self.title = title
        self.annotation = annotation
        self.full_text = full_text
        self.link = link
    def get_title(self):
        return self.title
    def get_annotaion(self):
        return self.annotation
    def get_full_text(self):
        return self.full_text
    def get_link(self):
        return self.link


class Joke:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text

class RBCNewsGrabber:
    def __init__(self, link):
        self.newspage_link = link

    def set_newspage_link(self, link):
        self.newspage_link = link

    def grab_news(n):
        try:
            response = requests.get(link, timeout=4)
            status = response.status_code
            if status == 404:
                raise InvalidUrlExcepion
            page = response.text
            soup = BeautifulSoup(contents, 'ixml')
            news_list = []
            for item in soup.find_all('item', limit=n):
                news = News(
        except:
            pass
    def check_internet_connection():

class JokesGrabber:



class TrollFactory:

class InternetConnectionException(Exception):

class PageParcingException(Exception):

class InvalidUrlExcepion(Exception):

if __name__ == __main__:
    grabber = RBCNewsGrabber('http://static.feed.rbc.ru/rbc/logical/footer/news.rss')

