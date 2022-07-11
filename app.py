#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from kutt import kutt

app = Flask(__name__)

API = ''


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shortenurl', methods=['GET', 'POST'])
def shortenurl():

    # For submit a new URL
    # obj variable has url object data (read the https://github.com/thedevs-network/kutt#api document)

    obj = kutt.submit(API, request.form['url'],
                      host_url='http://44.199.248.120:3000')
    if request.method == 'POST':
        return render_template('shortenurl.html', shorturl=obj['data']['link'].replace('https', 'http'))
    elif request.method == 'GET':
        return 'A GET request was made'
    else:
        return 'Not a valid request method for this route'
