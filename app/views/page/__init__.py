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
from app.models.myopia.HM_single_variant import HMSingleVariant
from app.models.myopia.rare_mac3_saige_lof import RareMac3SaigeLof
from app.models.myopia.rare_mac3_saige_damage import RareMac3SaigeDamage

page_bp = Blueprint('page', __name__)


@page_bp.get('/')
@page_bp.get('/index')
@page_bp.get('/index.html')
def index():
    return render_template('index.html')


@page_bp.get('/search_gene_result')
def search_gene_result():
    json = request.get_json(silent=True)
    args = request.args.to_dict()
    data = {**json, **args}
    search_content = str(data.get('search_content', ''))
    damage = RareMac3SaigeDamage.query.filter_by(gene=search_content).first_or_404()
    lof = RareMac3SaigeLof.query.filter_by(gene=search_content).first_or_404()
    return render_template('', damage=dict(damage), lof=dict(lof))
