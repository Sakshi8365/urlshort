import pyshorteners
import pyshorteners.shorteners
url = input('Enter the URL: ')

def urlshorten(url):
    a = pyshorteners.Shortener()
    print(a.tinyurl.short(url))


urlshorten(url)