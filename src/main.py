from flask import Flask, render_template, abort, request
import news
import json

app = Flask('app')

@app.route('/')
def index():
  #get article infos and stuff
  articles = []
  ordered_articles = news.get_articles_by_date()
  for title in ordered_articles:
    f = open("news/"+title+".json","r")
    content = json.loads(f.read())
    f.close()
    articles.append(content)
  print(len(articles))
  return render_template("index.html",articles=articles)

@app.route('/about')
def about():
  return render_template("about.html")

#incomplete stuff
@app.route('/article/<title>')
def article(title):
  try:
   f = open("news/"+title+".json","r")
   content = json.loads(f.read())
   f.close()
   return render_template("article.html",article=content)
  except:
    abort(404)

app.run(host='0.0.0.0', port=8080)