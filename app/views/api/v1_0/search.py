# -*- encoding: utf-8 -*-
"""
@File Name      :   search.py    
@Create Time    :   2021/9/25 10:30
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

from flask import request, Blueprint, g
from app.libs.error_exception import Success, NoDataError
from app.viewModels.myopia.search import search_classify_list, search_variant, search_gene

search_bp = Blueprint('search', __name__)


@search_bp.before_request
def handle_request():
    json = request.get_json(silent=True)
    args = request.args.to_dict()
    if json is not None and args is not None:
        data = {**json, **args}
        g.data = data


@search_bp.post('/list')
def search_list():
    content = str(g.data.get('content', ''))
    if content == '':
        return NoDataError('不能输入为空')
    classify = search_classify_list(content)
    data = [{'label': item, 'value': item} for item in classify]
    return Success(data=data)


@search_bp.post('/gene')
def search_gene():
    gene_name = str(g.data.get('gene_name', ''))
    if gene_name == '':
        return NoDataError('不能输入为空')
    return Success(data=search_gene(gene_name))


@search_bp.post('/variant')
def search_variant():
    SNP = str(g.data.get('SNP', ''))
    if SNP == '':
        return NoDataError('不能输入为空')
    return Success(data=search_variant(SNP))
