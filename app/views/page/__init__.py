# -*- encoding: utf-8 -*-
"""
@File Name      :   __init__.py.py    
@Create Time    :   2021/9/22 11:22
@Description    :   
@Version        :   
@License        :   
@Author         :   diklios
@Contact Email  :   diklios5768@gmail.com
@Github         :   https://github.com/diklios5768
@Blog           :   
@Motto          :   All our science, measured against reality, is primitive and childlike - and yet it is the most precious thing we have.
"""
__auth__ = 'diklios'

from flask import Blueprint, render_template, redirect,url_for
from app.viewModels.myopia.search import search_classify

page_bp = Blueprint('page', __name__)


@page_bp.get('/')
@page_bp.get('/index')
@page_bp.get('/index.html')
def index():
    return render_template('index.html')


@page_bp.get('/404')
def error_page():
    return render_template('404.html')


@page_bp.get('/result/<string:content>')
def result(content):
    if content == '':
        return redirect(url_for('myopia.page.error_page'))
    data = search_classify(content)
    if data == {}:
        return redirect(url_for('myopia.page.error_page'))
    else:
        return render_template('search_result_page.html', data=data)
