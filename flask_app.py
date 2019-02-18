from flask import Flask, render_template, json, request
from flask import Markup
import requests

app=Flask(__name__)
app.config["DEBUG"] = False


@app.route("/")
def index():
    headers = {
        'Authorization': 'Bearer key4aplWFBl8A764P',
    }

    params = (
        ('maxRecords', '250'),
        ('view', 'Grid view'),
    )


    r = requests.get('https://api.airtable.com/v0/appZCbeYkswEvX0ia/top250?api_key=key4aplWFBl8A764P')
    dict = r.json()
    dataset = []
    for i in dict['records']:
         dict = i['fields']
         dataset.append(dict)
    return render_template('table.html', entries=dataset)
