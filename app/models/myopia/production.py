# -*- encoding: utf-8 -*-
"""
@File Name      :   production.py    
@Create Time    :   2021/9/25 10:12
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

import click
from app.models.myopia.rare_mac3_saige_damage import init_rare_mac3_saige_damage
from app.models.myopia.rare_mac3_saige_lof import init_rare_mac3_saige_lof
from app.models.myopia.HM_single_variant import init_HM_single_variant
from app.utils.file_handler.table_handler.xlsx import read_xlsx


def init_production_data():
    table_rare_mac3_saige_damage = read_xlsx('app/models/myopia/source/rare_mac3_saige_damage_all.xlsx')
    init_rare_mac3_saige_damage(table_rare_mac3_saige_damage[1:])
    click.echo('rare_mac3_saige_damage finished')
    table_rare_mac3_saige_lof = read_xlsx('app/models/myopia/source/rare_mac3_saige_lof_all.xlsx')
    init_rare_mac3_saige_lof(table_rare_mac3_saige_lof[1:])
    click.echo('rare_mac3_saige_lof finished')
    table_HM_single_variant = read_xlsx('app/models/myopia/source/HM_single_variant.xlsx')
    init_HM_single_variant(table_HM_single_variant[1:])
    click.echo('HM_single_variant finished')


def update_production_data():
    pass
