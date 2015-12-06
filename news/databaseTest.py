# -*- conding: utf-8 -*-

from database import Database

db = Database()
for news in db.news_latest():
    print u"{0}\t{1}\t{2}".format(news["date"], news["category"], news["title"])
for news in db.news_latest(category="world", limit=10):
    print u"{0}\t{1}\t{2}".format(news["date"], news["category"], news["title"])
