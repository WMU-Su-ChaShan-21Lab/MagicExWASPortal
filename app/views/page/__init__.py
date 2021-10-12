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

from flask import request, Blueprint, render_template
from app.viewModels.myopia.search import search_gene_in_lof_and_damage
page_bp = Blueprint('page', __name__)


@page_bp.get('/')
@page_bp.get('/index')
@page_bp.get('/index.html')
def index():
    return render_template('index.html')


@page_bp.get('/search_gene_result/<string:gene_name>')
def search_gene_result(gene_name):
    data=search_gene_in_lof_and_damage(gene_name)
    return render_template('search_page.html',data=data)
