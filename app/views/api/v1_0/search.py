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
from app.libs.error_exception import Success, NoDataError
from app.models.myopia.HM_single_variant import HMSingleVariant
from app.models.myopia.rare_mac3_saige_lof import RareMac3SaigeLof
from app.models.myopia.rare_mac3_saige_damage import RareMac3SaigeDamage

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
    data = {}
    gene_name = g.data.get('gene_name', '')
    gene_damage = RareMac3SaigeDamage.query.filter_by(gene=gene_name).first()
    gene_lof = RareMac3SaigeLof.query.filter_by(gene=gene_name).first()
    if gene_damage is not None:
        data[''] = dict(gene_damage)
    if gene_lof is not None:
        data['lof'] = dict(gene_lof)
    if gene_lof is None and gene_damage is None:
        return NoDataError(chinese_msg='没有相应的数据')
    return Success(data=data)


@search_bp.post('/variant')
def search_variant():
    SNP = g.data.get('SNP', '')
    variant = HMSingleVariant.query.filter_by(SNP=SNP).first_or_404()
    return Success(data=dict(variant))
