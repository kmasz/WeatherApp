import feedparser
import ssl


news = 'https://www.tvn24.pl/najwazniejsze.xml'
def query_rss():
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    feed = []
    NewsFeed = feedparser.parse(news)
    #print(NewsFeed['items'][0])
    for item in NewsFeed['items']:
        #print(item['title'])
        tekst = item['summary_detail']['value'].split('/>')
        if len(tekst) > 1:
            #print(tekst[1].lstrip())
            feed.append([item['title'], tekst[1].lstrip()])
        else:
            #print(tekst[0])
            feed.append([item['title'], tekst[0]])
        #print(item['link'])
        #print("---")

    return feed
