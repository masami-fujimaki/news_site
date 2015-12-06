# -*- conding: utf-8 -*-

from datetime import datetime
from pymongo import DESCENDING, MongoClient

class Database:

    client = None
    db = None

    def __init__(self):
        if Database.client is None:
            Database.client = MongoClient('172.31.27.224')
            Database.db = Database.client.sankei
        else:
            print "already database connected."

    def news_find_one(self):
        news = Database.db.news
        return  news.find_one()

    def news_latest(self, limit=20, category=""):
        news = Database.db.news
        if category == "":
            return news.find().sort("date", DESCENDING).limit(limit)
        else:
            return news.find({"category": category}).sort("date", DESCENDING).limit(limit)

    def news_date(self, date, category=""):
        start_date = datetime(date.year,date.month,date.day,0,0,0)
        end_date = datetime(date.year,date.month,date.day,23,59,59)
        news = Database.db.news
        if category == "":
            return news.find({"date":{"$gte":start_date, "$lte":end_date}}).sort("date", DESCENDING)
        else:
            return news.find({"category": category, "date":{"$gte":start_date, "$lte":end_date}}).sort("date", DESCENDING)
