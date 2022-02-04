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
    req = re.sub('\[.*?\]', '', req)
    req = re.sub('[%s]' % re.escape(string.punctuation), '', req)
    req = re.sub('\s+', ' ', req)
    alc_cont = ''
    alc_cont = req.split(' ').pop(1)
    print('alcohol content = ' + alc_cont)

# #test
# #shivagi
# print('Shivaaji')
# url_alc_imdb('https://www.imdb.com/title/tt0479751/parentalguide')
# print('Bahubali')
# #bahubali
# url_alc_imdb('https://www.imdb.com/title/tt2631186/parentalguide')

# #2015
def get_URL_list(url):
    response = requests.get(url).text
    html_document = getHTMLdocument(url_to_scrape)
    soup = BeautifulSoup(html_document, 'lxml')
    text = [link.get('href') for link in soup.find_all('a', 
                          attrs={'href': re.compile("^\/title")})]
    preURL = 'https://www.imdb.com'
    postURL = 'parentalguide'
    url_list = []
    i=0
    for x in text:
        x = preURL + x + postURL
        url_list.append(x)
    print(url_list)

def get_movie_title_list(url):
    html_document = getHTMLdocument(url)
    soup = BeautifulSoup(html_document, 'lxml')  
    text = [link.text for link in soup.find_all('a', attrs={'href': re.compile("^\/title")})]

    print(text)  
    
movie_list_2015_url = "https://www.imdb.com/list/ls076765584/"
get_URL_list(movie_list_2015_url)
get_movie_title_list(movie_list_2015_url)
