#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api
from rss_test import query_rss
from datetime import datetime
import pytz
app = Flask(__name__)
@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name':'3088171'}, {'name':'Montreal'}, {'name':'Calgary'},
        {'name':'Ottawa'}, {'name':'Edmonton'}, {'name':'Mississauga'},
        {'name':'Winnipeg'}, {'name':'Vancouver'}, {'name':'Brampton'}, 
        {'name':'Quebec'}])
@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    news = query_rss()
    #pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error,
        news=news)

## przekazanie fuknkcji do temlpate html
@app.context_processor
def some_processor():
    def date2string(date):
        try:
            datastr = pytz.utc.localize(datetime.utcfromtimestamp(date)).strftime("%d-%m-%Y")
            timestr = pytz.utc.localize(datetime.utcfromtimestamp(date)).strftime("%H:%M")
        except Exception as exc:
            print(exc)
            datastr = None
            timestr = None
        return [datastr, timestr]
    return {'date2string': date2string}

if __name__=='__main__':
    app.run(debug=True)
