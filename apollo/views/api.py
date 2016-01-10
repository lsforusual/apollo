#!/usr/bin/env python
#coding=utf-8

import requests
import json
import datetime

from flask import Module, Response, request, flash, jsonify, g, current_app,\
    abort, redirect, url_for, session, render_template

from flask.ext.login import login_required,current_user

from apollo.models import Book,BorrowLog,Tag,BookTag
from apollo.extensions import db
from apollo.helpers import DoubanClient

api = Module(__name__)

# 获取豆瓣图书信息
@api.route("/douban_book_info/", methods=("GET","POST"))
def douban_book_info():
    isbn = request.args.get('isbn', '')
    print "douban_book_info , isbn=",isbn

    r = requests.get('http://api.douban.com/v2/book/isbn/%s' % isbn)

    return r.text
