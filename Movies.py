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
    if(alc_cont == 'Be'):
        alc_cont = 'Unrated'
    #print(alc_cont)
    return alc_cont
    #return text

def get_URL_list(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    text = [link.get('href') for link in soup.find_all('a', 
                          attrs={'href': re.compile("^\/title\/[t]{2}[0-9]{7}\/$")})]
    preURL = 'https://www.imdb.com'
    postURL = 'parentalguide'
    url_list = []
    i=0
    for x in text:
        x = preURL + x + postURL
        url_list.append(x)
    #print(url_list)
    return url_list
def get_movie_title_list(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')  
    text = [link.text for link in soup.find_all('a', attrs={'href': re.compile("^\/title")})]
     
    for x in text:
        if(x==' \n'):
            text.remove(' \n')
        
            
    #print(text)
    return text

#URL OF TOP TAMIL MOVIES LIST
movie_list_2015_url = 'https://www.imdb.com/list/ls031392332/'
movie_list_2016_url = 'https://www.imdb.com/list/ls064266039/'
movie_list_2017_url = 'https://www.imdb.com/list/ls069242710/'
movie_list_2018_url = 'https://www.imdb.com/list/ls045861940/'
movie_list_2019_url = 'https://www.imdb.com/list/ls041663030/'
movie_list_2020_url = 'https://www.imdb.com/list/ls097124558/'
movie_list_2021_url = 'https://www.imdb.com/list/ls084663427/'

#movie_urls_list = ['https://www.imdb.com/list/ls031392332/', 'https://www.imdb.com/list/ls064266039/','https://www.imdb.com/list/ls069242710/', 'https://www.imdb.com/list/ls045861940/','https://www.imdb.com/list/ls041663030/', 'https://www.imdb.com/list/ls097124558/','https://www.imdb.com/list/ls084663427/']

# movie_titles = []
# movie_urls = []
# movie_urls = [get_URL_list(u) for u in movie_urls]
# movie_titles = [get_movie_title_list(u) for u in movie_urls]


#GETTING EACH YEARS DETAILS IN THE FORM OF A LIST
print("**2015 MOVIES**")
u1 = get_URL_list(movie_list_2015_url)
t1 = get_movie_title_list(movie_list_2015_url)

print("**2016 MOVIES**")
u2 = get_URL_list(movie_list_2016_url)
t2 = get_movie_title_list(movie_list_2016_url)

print("**2017 MOVIES**")
u3 = get_URL_list(movie_list_2017_url)
t3 = get_movie_title_list(movie_list_2017_url)

print("**2018 MOVIES**")
u4 = get_URL_list(movie_list_2018_url)
t4 = get_movie_title_list(movie_list_2018_url)

print("**2019 MOVIES**")
u5 = get_URL_list(movie_list_2019_url)
t5 = get_movie_title_list(movie_list_2019_url)

print("**2020 MOVIES**")
u6 = get_URL_list(movie_list_2020_url)
t6 = get_movie_title_list(movie_list_2020_url)

print("**2021 MOVIES**")
u7 = get_URL_list(movie_list_2021_url)
t7 = get_movie_title_list(movie_list_2021_url)

all_movie_titles = []
all_movie_links = []
all_movie_titles = t1 + t2 + t3 + t4 + t5 + t6 + t7
all_movie_links = u1 + u2 + u3 + u4 + u5 + u6 + u7
print(all_movie_titles)
print(all_movie_links)

alc_content_movie = []
for x in all_movie_links:
    
    alc_content_movie.append(url_alc_imdb(x))

print(alc_content_movie)
