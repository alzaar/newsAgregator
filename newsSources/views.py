from rest_framework.views import APIView
from rest_framework.response import Response
from .news_crawler import NewsCrawler

class News(APIView):

    def get(self, request):
        dawn = NewsCrawler().get_articles(url='http://www.dawn.com', class_name='story__link')
        hacker_news = NewsCrawler().get_articles(url='https://news.ycombinator.com', class_name='storylink')
        globe_mail = NewsCrawler().get_articles(url='https://www.theglobeandmail.com', class_name='c-card__grid c-card__link', route=True)
        tech_crunch = NewsCrawler().get_articles(url='https://techcrunch.com', class_name='post-block__title__link')
        guardian = NewsCrawler().get_articles(url='https://www.theguardian.com/international', class_name='u-faux-block-link__overlay js-headline-text')

        return Response({ 
            'sources': {
                'dawn': dawn,
                'hackerNews': hacker_news,
                'globeMail': globe_mail,
                'techCrunch': tech_crunch,
                'guardian': guardian
                } 
            })
