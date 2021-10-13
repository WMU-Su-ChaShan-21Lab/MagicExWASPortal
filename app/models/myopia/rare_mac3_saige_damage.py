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
    Pvalue_FET = Column(String(20))
    Pvalue_burden = Column(String(20))
    Pvalue_SKAT = Column(String(20))
    Pvalue_SKAT_O = Column(String(20))
    Pvalue_ACAT_V = Column(String(20))
    Pvalue_ACAT_O = Column(String(20))
    Pvalue_SAIGE = Column(String(20))
    participants = Column(Integer)
    case = Column(Integer)
    case_wild = Column(Integer)
    control = Column(Integer)
    control_wild = Column(Integer)
    pro_cases_with_QV = Column(String(20))
    pro_control_with_QV = Column(String(20))
    odds_ratio = Column(String(20))
    CI1 = Column(String(20))
    CI2 = Column(String(20))

    fields = ['gene', 'Phenotype', 'QV', 'Pvalue_FET', 'Pvalue_burden', 'Pvalue_SKAT', 'Pvalue_SKAT_O', 'Pvalue_ACAT_V',
              'Pvalue_ACAT_O', 'Pvalue_SAIGE', 'participants', 'case', 'case_wild', 'control', 'control_wild',
              'pro_cases_with_QV', 'pro_control_with_QV', 'odds_ratio', 'CI1', 'CI2']


def init_rare_mac3_saige_damage(table: list):
    with db.auto_commit():
        for row in table:
            new_row = RareMac3SaigeDamage()
            attrs = {
                'gene': row[0],
                'Phenotype': row[1],
                'QV': row[2],
                'Pvalue_FET': row[3],
                'Pvalue_burden': row[4],
                'Pvalue_SKAT': row[5],
                'Pvalue_SKAT_O': row[6],
                'Pvalue_ACAT_V': row[7],
                'Pvalue_ACAT_O': row[8],
                'Pvalue_SAIGE': row[9],
                'participants': row[10],
                'case': row[11],
                'case_wild': row[12],
                'control': row[13],
                'control_wild': row[14],
                'pro_cases_with_QV': row[15],
                'pro_control_with_QV': row[16],
                'odds_ratio': row[17],
                'CI1': row[18],
                'CI2': row[19],





            }
            new_row.set_attrs(attrs)
            db.session.add(new_row)
