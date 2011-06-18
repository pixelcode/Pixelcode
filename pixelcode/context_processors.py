from models import *
import twitter
from django.core.cache import cache
from django.conf import settings

def main(request):
    context = { 'navigations' : Navigation.objects.filter(publish=True), }
    return context

def parse_tweet(tweet):
    import re
    handles = re.findall('\@.*?\w+', tweet)
    links = re.findall(r'http://?([^\'" >]+)', tweet)
    for handle in handles:
        tweet = tweet.replace(handle, '<a href="http://www.twitter.com/'+handle.replace('@', '')+'" target="_blank">'+handle+'</a>')
    for link in links:
        link = link.strip()
        tweet = tweet.replace('http://'+link, '<a href="http://'+link+'" target="_blank">http://'+link+'</a>')
    return tweet
    
def latest_tweet( request ):
    tweets = cache.get('tweets')
    #if not tweets:
    #    tweets = twitter.Api().GetUserTimeline( settings.TWITTER_USER )[0:8]
    #    for t in tweets:
    #        t.text = parse_tweet(t.text)
    #        t.date = datetime.strptime( t.created_at, "%a %b %d %H:%M:%S +0000 %Y" )
    #    cache.set('tweets', tweets, settings.TWITTER_TIMEOUT )
    return { "tweets": tweets }