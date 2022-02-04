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
    
#URL OF TOP TAMIL MOVIES LIST
movie_list_2015_url = 'https://www.imdb.com/list/ls031392332/'
movie_list_2016_url = 'https://www.imdb.com/list/ls064266039/'
movie_list_2017_url = 'https://www.imdb.com/list/ls069242710/'
movie_list_2018_url = 'https://www.imdb.com/list/ls045861940/'
movie_list_2019_url = 'https://www.imdb.com/list/ls041663030/'
movie_list_2020_url = 'https://www.imdb.com/list/ls097124558/'
movie_list_2021_url = 'https://www.imdb.com/list/ls084663427/'

#GETTING EACH YEARS DETAILS IN THE FORM OF A LIST
print("**2015 MOVIES**")
get_URL_list(movie_list_2015_url)
get_movie_title_list(movie_list_2015_url)

print("**2016 MOVIES**")
get_URL_list(movie_list_2016_url)
get_movie_title_list(movie_list_2016_url)

print("**2017 MOVIES**")
get_URL_list(movie_list_2017_url)
get_movie_title_list(movie_list_2017_url)

print("**2018 MOVIES**")
get_URL_list(movie_list_2018_url)
get_movie_title_list(movie_list_2018_url)

print("**2019 MOVIES**")
get_URL_list(movie_list_2019_url)
get_movie_title_list(movie_list_2019_url)

print("**2020 MOVIES**")
get_URL_list(movie_list_2020_url)
get_movie_title_list(movie_list_2020_url)

print("**2021 MOVIES**")
get_URL_list(movie_list_2021_url)
get_movie_title_list(movie_list_2021_url)
