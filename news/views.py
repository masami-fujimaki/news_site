# -*- coding: utf-8 -*-
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext

from bson.json_util import dumps

from database import Database

# Create your views here.

def index(request):
    param_date = request.GET.get("date")
    if param_date is None:
        date = datetime.today()
        news = Database().news_latest(limit=50)
    else:
        date = datetime.strptime(param_date, "%Y-%m-%d") 
        news = Database().news_date(date)
    return render_to_response(
        'index.html', 
        {
          'news': _data_date_to_string(news), 
          'date': date,
          'categories': _categories(),
        },
        context_instance=RequestContext(request))


def category(request, category):
    param_date = request.GET.get("date")
    if param_date is None:
        date = datetime.today()
        news = Database().news_latest(category=category, limit=50)
    else:
        date = datetime.strptime(param_date, "%Y-%m-%d") 
        news = Database().news_date(date, category=category)
    return render_to_response(
        'index.html', 
        {
          'news': _data_date_to_string(news), 
          'category': category, 
          'date': date,
          'categories': _categories(),
        },
        context_instance=RequestContext(request))


def _categories() :
    return ["economy","politics","world","sports","entertainments","life","All"];

def _data_date_to_string(datas):
    news = []
    for data in datas:
        data['date'] = data['date'].strftime("%Y/%m/%d %H:%M")
        news.append(data)
    return news 


def _render_json_response(request, data, status=None):
    '''response を JSON で返却'''
    json_str = dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response
