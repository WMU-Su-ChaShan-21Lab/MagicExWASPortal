from itertools import chain

from app.libs.error_exception import NoDataError
from app.models.myopia.HM_single_variant import HMSingleVariant
from app.models.myopia.rare_mac3_saige_lof import RareMac3SaigeLof
from app.models.myopia.rare_mac3_saige_damage import RareMac3SaigeDamage


def search_gene_list(content):
    damage_result = RareMac3SaigeDamage.query.with_entities(RareMac3SaigeDamage.gene).filter(
        RareMac3SaigeDamage.gene.like('%' + content + '%')).all()
    lof_result = RareMac3SaigeLof.query.with_entities(RareMac3SaigeLof.gene).filter(
        RareMac3SaigeLof.gene.like('%' + content + '%')).all()
    return list(set([*list(chain(*damage_result)), *list(chain(*lof_result))]))


def search_variant_list(content):
    variants_result = HMSingleVariant.query.with_entities(HMSingleVariant.SNP).filter(
        HMSingleVariant.SNP.like('%' + content + '%')).all()
    return [variant[0] for variant in variants_result]


def search_classify_list(content):
    if content.find(':') == -1:
        return search_gene_list(content)
    else:
        return search_variant_list(content)


def search_gene(gene_name):
    data = {}
    gene_damage = RareMac3SaigeDamage.query.filter_by(gene=gene_name).first()
    gene_lof = RareMac3SaigeLof.query.filter_by(gene=gene_name).first()
    if gene_damage is not None:
        data['damage'] = dict(gene_damage)
    if gene_lof is not None:
        data['lof'] = dict(gene_lof)
    if gene_lof is None and gene_damage is None:
        return NoDataError(chinese_msg='没有相应的数据')
    return data


def search_variant(SNP_name):
    data = {}
    variant = HMSingleVariant.query.filter_by(SNP=SNP_name).first()
    if variant is not None:
        data['variant'] = dict(variant)
    return data


def search_classify(content: str):
    if content.find(':') == -1:
        return search_gene(content)
    else:
        return search_variant(content)
