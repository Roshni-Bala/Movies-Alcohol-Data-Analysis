import requests
from bs4 import BeautifulSoup
import re
import string
import numpy as np

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

def unique(url):
    seen = set()
    seen_add = seen.add
    return [x for x in url if not (x in seen or seen_add(x))]

#unique(all_movie_links)

def get_URL_list(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    text = [link.get('href') for link in soup.find_all('a', 
                          attrs={'href': re.compile("^\/title\/[t]{2}[0-9]{4,10}\/$")})]
    preURL = 'https://www.imdb.com'
    postURL = 'parentalguide'
    url_list = []
    i=0
    for x in text:
        x = preURL + x + postURL
        url_list.append(x)
    #url_list = list(set(url_list))
    url_list = unique(url_list)
    print(url_list)
    return url_list


        
def get_movie_title_list(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')  
    title_list = [link.text for link in soup.find_all('a', attrs={'href': re.compile("^\/title")})]
    
    for x in title_list:
        if(x==' \n'):
            title_list.remove(' \n')
    for x in title_list:      
        if(x=='See full summary'):
            title_list.remove('See full summary')
    print(title_list)
        
            
    #print(text)
    return title_list


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
#print(u1)
#print(t1)
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


alc_content_movie = []
for x in all_movie_links:
    
    alc_content_movie.append(url_alc_imdb(x))

print(alc_content_movie)

import pandas as pd


dict = {'Movie Name':all_movie_titles, 'IMDB Link':all_movie_links, 'Alcoholism Displayed':alc_content_movie}
df1 = pd.DataFrame({'Movie Name':all_movie_titles})
df2 = pd.DataFrame({'IMDB Link':all_movie_links})
df3 = pd.DataFrame({'Alcoholism Displayed':alc_content_movie})

df1 = df1.reset_index()
df2 = df2.reset_index()
df3 = df3.reset_index()
df = [df1, df2, df3]

df_final = pd.concat(df, axis=1)
df_final.to_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\moviesdataset.csv', index=False)
