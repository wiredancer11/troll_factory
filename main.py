import requests
import csv
from bs4 import BeautifulSoup
from sketch import Sketch

class News:
    def __init__(self,title, description, full_text, link):
        self.title = title
        self.description= description
        self.full_text = full_text
        self.link = link
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
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
        self.news_list = []

    def set_newspage_link(self, link):
        self.newspage_link = link

    def grab_news(self, n):
        try:
            response = requests.get(self.newspage_link, timeout=4)
            status = response.status_code
            if status == 404:
                raise InvalidUrlExcepion
            page = response.text
            soup = BeautifulSoup(page,  'xml')
            self.news_list = []
            for item in soup.find_all('item', limit=n):
                title= item.find('title').text
                description = item.find('description').text
                full_text = item.find('rbc_news:full-text').text
                link = item.find('link').text
                news = News(title, description, full_text, link)
                self.news_list.append(news)
        except Exception as e:
            print(e)
    def check_internet_connection():
        pass

class JokesGrabber:
    def __init__(self):
        self.jokes_file = ''

    def cache_jokes(self):
        i = 0
        page = 2
        try:
            with open('jokes.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                while i < 1000:
                    link = f"https://www.anekdot.ru/tags/%D0%BE%20%D0%B6%D0%B8%D0%B7%D0%BD%D0%B8/{page}?type=anekdots"
                    response = requests.get(link, timeout=4)
                    status = response.status_code
                    if status == 404:
                        raise InvalidUrlExcepion
                    html = response.text
                    soup = BeautifulSoup(html,  'html.parser')
                    for item in soup.findAll("div", class_="text"):
                        i+=1

                        writer.writerow([item.text])
                    page += 1
        except Exception as e:
             print(e)
    def get_jokes(self, n):
        jokes_list = []
        with open('jokes.csv', newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
            for i in range(n):
                joke = Joke(rows[i][0])
                jokes_list.append(joke)
        return jokes_list




class TrollFactory:
    def __init__(self, jokes):
        self.jokes = jokes

    def jokefy(self, news):
        similar_joke = None
        closest_similarity = -1
        news_sketch = Sketch(news.description, 2, 50)
        for joke in self.jokes:
            joke_sketch = Sketch(joke.text, 2, 50)
            similarity = joke_sketch.similarTo(news_sketch)
            if similarity > closest_similarity:
                similar_joke = joke
                closest_similarity = similarity
        news.full_text = similar_joke.text

    def save(self):
        grabber = RBCNewsGrabber('http://static.feed.rbc.ru/rbc/logical/footer/news.rss')
        grabber.grab_news(8)
        news_list = grabber.news_list
        with open('output.txt', 'w') as f:
            for news in news_list:
                self.jokefy(news)
                f.write(news.title + "\n\n")
                f.write(news.description+ "\n\n")
                f.write(news.full_text+ "\n------------\n")



class InternetConnectionException(Exception):
    pass

class PageParcingException(Exception):
    pass

class InvalidUrlExcepion(Exception):
    pass

if __name__ == "__main__":
    jokes_grabber = JokesGrabber()
    factory = TrollFactory(jokes_grabber.get_jokes(1000))
    factory.save()
