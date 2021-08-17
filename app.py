from bs4 import BeautifulSoup
import requests
from flask import *
import json

app = Flask(__name__)

#Get page html
def get_data(url):
    header = {'User-Agent': 'Mozilla/5.0'}
    soup = BeautifulSoup(requests.get(url,headers=header).content, 'lxml')
    return soup

#main news template
def getNews(search_query):
    url = f'https://news.google.com/search?q={search_query}'
    response = get_data(url).find_all('div',{'class':'NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc'})    

    searchList = []
    for item in response:
        try:
            newsItem = {
                'title':item.find('article').find('h3').find('a').text,
                'url':'https://news.google.com'+item.find('article').find('h3').find('a')['href'][1:],
                'img':item.find('figure').find('img')['src'],
                'author':'in article',
                'source':item.find('article').find('div').find('div').find('a').text,
                'date':item.find('article').find('div').find('div').find('time')['datetime'],
            }
            searchList.append(newsItem) 
        except:
             print('error')
    
    return searchList

#Search
@app.route('/news/everything/', methods=['GET'])
def searchEndPoint():
    search_query = request.args.get('q') # /news/everything/?q=Mohamed salah
    newsList = getNews(search_query)
    searchList = {'total_results':len(newsList),'query':search_query,'data':newsList}
    return json.dumps(searchList)

if __name__ == '__main__':
  app.run(port=7775)