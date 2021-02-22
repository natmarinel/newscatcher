from django.shortcuts import render, redirect
from GoogleNews import GoogleNews
import tweepy
from tweepy import OAuthHandler
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Create your views here.

def googleNewsApi(request, word):

    googlenews = GoogleNews()
    googlenews.set_lang('en')
    googlenews.set_period('7d')
    googlenews.set_encode('utf-8')
    googlenews.get_news(str(word))
    googlenews.total_count()
    resultsGoogleNews = googlenews.results()
    #print(resultsGoogleNews)
    #print(googlenews.total_count())

    #TWITTER
    consumer_key = 'sz6x0nvL0ls9wacR64MZu23z4'
    consumer_secret = 'ofeGnzduikcHX6iaQMqBCIJ666m6nXAQACIAXMJaFhmC6rjRmT'
    access_token = '854004678127910913-PUPfQYxIjpBWjXOgE25kys8kmDJdY0G'
    access_token_secret = 'BC2TxbhKXkdkZ91DXofF7GX8p2JNfbpHqhshW1bwQkgxN'
    # create OAuthHandler object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # set access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # create tweepy API object to fetch tweets
    api = tweepy.API(auth)
    date_since = datetime.today().strftime('%Y-%m-%d')
    print(date_since)
    #tweets = api.search(str("bitcoin"), count=1)
    tweets = tweepy.Cursor(api.search,
              q= str(word),
              lang="en",
              since=date_since).items(100)
    """print(tweets.__dict__['page_iterator'].__dict__)
    for tweet in tweets:
        print(tweet)
        print(tweet.id)"""
    #return googlenews
    """for result in resultsGoogleNews:

        title = result['title']
        date = result['date']
        link = result['link']
        source = result['site']

        news = {'title':title, 'date': date, 'link': link, 'site':site}
    """
    return render(request, 'homepage.html', {'news':resultsGoogleNews, 'tweets':tweets})
        


def search(request):
    """request = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=BTCUSDT')
    request.json()
    btc = request['price']
    ethBinance = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=BTCUSDT')
    ethBinance.json()
    ETH = ethBinance['price']
    price = {'btc':BTC,'eth':ETH}"""
    symbols = ['BTCUSDT', 'ETHUSDT', 'LTCUSDT', 'BCHUSDT', 'EGLDUSDT', 'DOTUSDT', 'LINKUSDT']
    i = 0
    price = []
    for symbol in symbols:
        response = requests.get('https://api.binance.com/api/v1/ticker/price?symbol='+symbol)
        price.append(response.json())
        print(price)

    q = request.GET.get("q", None)
    if q:
        print(q)
        word = request.GET.get('q')
        return googleNewsApi(request, word)
    else:
        return render(request,'search.html', {'prices':price})


def get_tweets(request):

    """consumer_key = 'sz6x0nvL0ls9wacR64MZu23z4'
    consumer_secret = 'ofeGnzduikcHX6iaQMqBCIJ666m6nXAQACIAXMJaFhmC6rjRmT'
    access_token = '854004678127910913-PUPfQYxIjpBWjXOgE25kys8kmDJdY0G'
    access_token_secret = 'BC2TxbhKXkdkZ91DXofF7GX8p2JNfbpHqhshW1bwQkgxN'
    # create OAuthHandler object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # set access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # create tweepy API object to fetch tweets
    api = tweepy.API(auth)
    date_since = datetime.today().strftime('%Y-%m-%d')
    print(date_since)
    #tweets = api.search(str("bitcoin"), count=1)
    tweets = tweepy.Cursor(api.search,
              q="#bitcoin",
              lang="en",
              since="2021-02-17").items(100)
    print(tweets.__dict__)
    for tweet in tweets:
        print(tweet.text)
        #print(tweet)
        print(tweet.created_at)
        print(tweet.user.name)
        print(tweet.urls.expanded_url)
    """
    response = requests.get('https://news.search.yahoo.com/search?p=bitcoin')
    #print(response.__dict__)
    
    soup = BeautifulSoup(response.text)
    #print(soup)
    news = soup.find_all('div', attrs={'class': 'NewsArticle'})

    for new in news:

        #soup = BeautifulSoup(news)
        links = new.find('a', attrs={'class': 'thmb'})
        print("link:",links)


        link = links.select('href')
        print(link.__dict__)

    


    #print(news)