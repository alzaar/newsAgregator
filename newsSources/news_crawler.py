import requests
from bs4 import BeautifulSoup

class NewsCrawler():

    def get_articles(self, url, class_name, route=False):
        res = requests.get(url).text
        soup = BeautifulSoup(res, 'html.parser')
        article_elements = soup.findAll("a", {"class": class_name})

        parsed_articles = []
        count = 1
        for ele in article_elements:
            
            article = {
                'id': count,
                'title': ele.text.strip(),
                'link': ele['href'] if not route else url + ele['href'] 
            }

            count += 1
            parsed_articles.append(article)

        return parsed_articles