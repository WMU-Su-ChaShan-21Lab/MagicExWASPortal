# -*- encoding: utf-8 -*-
"""
@File Name      :   rare_mac3_saige_damage.py    
@Create Time    :   2021/9/22 11:26
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

from app.models import db
from app.models.base import Base
from sqlalchemy import Column, Float, String, Integer


class RareMac3SaigeDamage(Base):
    __tablename__ = 'rare_mac3_saige_damage'
    gene = Column(String(20), default='')
    Phenotype = Column(String(10), default='HM')
    QV = Column(String(10))
    case = Column(Integer)
    case_wild = Column(Integer)
    control = Column(Integer)
    control_wild = Column(Integer)
    p_value_FET = Column(String(20))
    odds_ratio = Column(String(20))
    CI1 = Column(String(20))
    CI2 = Column(String(20))
    burden_p1 = Column(String(20))
    skat_p1 = Column(String(20))
    acatv_p1 = Column(String(20))
    skato_p1 = Column(String(20))
    acato_p = Column(String(20))
    Pvalue_SAIGE = Column(String(20))
    participants = Column(Integer)
    pro_cases_with_QV = Column(String(20))
    pro_control_with_QV = Column(String(20))

    fields = ['id', 'gene', 'Phenotype', 'QV', 'case', 'case_wild', 'control', 'control_wild', 'p_value_FET',
              'odds_ratio', 'CI1', 'CI2', 'burden_p1', 'skat_p1', 'acatv_p1',
              'skato_p1', 'acato_p', 'Pvalue_SAIGE', 'participants', 'pro_cases_with_QV', 'pro_control_with_QV']


def init_rare_mac3_saige_damage(table: list):
    with db.auto_commit():
        for row in table:
            new_row = RareMac3SaigeDamage()
            attrs = {
                'gene': row[0],
                'Phenotype': row[1],
                'QV': row[2],
                'case': row[3],
                'case_wild': row[4],
                'control': row[5],
                'control_wild': row[6],
                'p_value_FET': row[7],
                'odds_ratio': row[8],
                'CI1': row[9],
                'CI2': row[10],
                'burden_p1': row[11],
                'skat_p1': row[12],
                'acatv_p1': row[13],
                'skato_p1': row[14],
                'acato_p': row[15],
                'Pvalue_SAIGE': row[16],
                'participants': row[17],
                'pro_cases_with_QV': row[18],
                'pro_control_with_QV': row[19],
            }
            new_row.set_attrs(attrs)
            db.session.add(new_row)
