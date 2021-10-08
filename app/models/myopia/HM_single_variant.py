# -*- encoding: utf-8 -*-
"""
@File Name      :   HM_single_variant.py    
@Create Time    :   2021/9/25 8:05
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


class HMSingleVariant(Base):
    __tablename__ = 'HM_single_variant'
    SNP = Column(String(200), default='')
    CHR = Column(Integer)
    BP = Column(String(200), default='')
    REF = Column(String(200), default='')
    ALT = Column(String(200), default='')
    Beta = Column(String(20))
    SE = Column(String(20))
    OR = Column(String(20))
    MLMA_LOCO = Column(String(20))
    MLMA = Column(String(20))
    EMMAX = Column(String(20))
    Logistic = Column(String(20))

    fields = ['id', 'SNP', 'CHR', 'BP', 'REF', 'ALT', 'Beta', 'SE', 'OR', 'MLMA_LOCO', 'MLMA', 'EMMAX', 'Logistic']


def init_HM_single_variant(table: list):
    with db.auto_commit():
        for row in table:
            new_row = HMSingleVariant()
            attrs = {
                'SNP': row[0],
                'CHR': row[1],
                'BP': row[2],
                'REF': row[3],
                'ALT': row[4],
                'Beta': row[5],
                'SE': row[6],
                'OR': row[7],
                'MLMA_LOCO': row[8],
                'MLMA': row[9],
                'EMMAX': row[10],
                'Logistic': row[11],
            }
            new_row.set_attrs(attrs)
            db.session.add(new_row)
