#process /news and return stuff
import json, os
from datetime import datetime

def insertionSort(articles): 
    result = list(articles.keys())
    #5, 4, 7, 2
    for i in range(1, len(articles)):
      key = result[i]
      while 0 <= i-1:
        before = result[i-1]
        #if selected date is bigger then date before, swap
        if articles[key] > articles[before]:
          old = result[i-1]
          print(old)
          result[i-1] = result[i]
          result[i] = old
          i-=1
        else: 
          break

    return result

def get_article(title):
  f = open('news/'+title+'.json','r')
  content = json.loads(f.read())
  f.close()
  return content

def get_all_articles():
  dir = os.scandir("/news")
  files = [f.name.split('.')[0] for f in dir]
  files.remove('__articles__')
  return files

def get_articles_by_date():
  f = open("news/__articles__.json","r")
  content = json.loads(f.read())
  f.close()
  #sort articles by date
  articles = {}
  for article in content['date'].items():
    articles[article[0]] = datetime.strptime(article[1], "%m/%d/%y")
  return insertionSort(articles)
  
#sections: World, Economy, US, Other