import pickle
import requests
from bs4 import BeautifulSoup
import re
import string

def url_alc_imdb(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find('section', id = "advisory-alcohol")]
    req = text[3]
    #test = text.lower()
    #test = re.sub('\[.*?\]', '', test)
    #text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    #text = re.sub('\w*\d\w*', '', text)
    #print(text)
    req.lower()
    req = re.sub('\[.*?\]', '', req)
    req = re.sub('[%s]' % re.escape(string.punctuation), '', req)
    req = re.sub('\s+', ' ', req)
    #req = re.sub('\w*\d\w*', '', req)
    print('required = ' + req)
    
    
    #return text

url_alc_imdb('https://www.imdb.com/title/tt0479751/parentalguide')
print('hey')
url_alc_imdb('https://www.imdb.com/title/tt2631186/parentalguide')
    
