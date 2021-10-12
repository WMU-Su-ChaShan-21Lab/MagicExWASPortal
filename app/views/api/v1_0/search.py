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
from itertools import chain
from app.libs.error_exception import Success
from app.models.myopia.HM_single_variant import HMSingleVariant
from app.models.myopia.rare_mac3_saige_lof import RareMac3SaigeLof
from app.models.myopia.rare_mac3_saige_damage import RareMac3SaigeDamage
from app.viewModels.myopia.search import search_gene_in_lof_and_damage

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
    gene_name = str(g.data.get('gene_name', ''))
    rare_mac3_saige_damage_result = RareMac3SaigeDamage.query.with_entities(RareMac3SaigeDamage.gene).filter(
        RareMac3SaigeDamage.gene.like('%' + gene_name + '%')).all()
    rare_mac3_saige_lof_result = RareMac3SaigeLof.query.with_entities(RareMac3SaigeLof.gene).filter(
        RareMac3SaigeLof.gene.like('%' + gene_name + '%')).all()
    return Success(
        data=list(set([*list(chain(*rare_mac3_saige_damage_result)), *list(chain(*rare_mac3_saige_lof_result))])))


@search_bp.post('/gene')
def search_gene():
    gene_name = g.data.get('gene_name', '')
    return Success(data=search_gene_in_lof_and_damage(gene_name))


@search_bp.post('/variant')
def search_variant():
    SNP = g.data.get('SNP', '')
    variant = HMSingleVariant.query.filter_by(SNP=SNP).first_or_404()
    return Success(data=dict(variant))
