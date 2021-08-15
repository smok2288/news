from django.shortcuts import render
import requests
from bs4 import BeautifulSoup



tut = 'https://news.tut.by/?sort=time#sort'
onliner = 'https://www.onliner.by'
lh= 'https://lifehacker.ru'

tut_list = []
onliner_list=[]


def get_tut():
    r = requests.get(tut).text
    soup = BeautifulSoup(r,'lxml')
    posts = soup.find_all('div', class_='news-section m-sorted')
    for post in posts:
        title= post.find('div', class_='news-entry small pic time ni').text
        url = post.find('a').get('href')
        data = {'title':title,
                'url':url}
        tut_list.append(data)

get_tut()


def get_onliner():
    r = requests.get(onliner).text
    soup = BeautifulSoup(r,'lxml')
    posts = soup.find_all('ul', class_='b-teasers-2 cfix')
    for post in posts:
        title = post.find('a', class_='b-teasers-2__teaser-i').text
        url = post.find('a').get('href')
        print(url)
        data = {'title':title,
                'url':url}
        onliner_list.append(data)

get_onliner()


def home(requests):
    context = {
        "tut_list":tut_list,
        'onliner_list':onliner_list,
    }
    return render(requests, 'news_app/home.html',context)


