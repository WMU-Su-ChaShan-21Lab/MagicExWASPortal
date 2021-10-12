from app.libs.error_exception import NoDataError
from app.models.myopia.HM_single_variant import HMSingleVariant
from app.models.myopia.rare_mac3_saige_lof import RareMac3SaigeLof
from app.models.myopia.rare_mac3_saige_damage import RareMac3SaigeDamage


def search_gene_in_lof_and_damage(gene_name):
    data = {}
    gene_damage = RareMac3SaigeDamage.query.filter_by(gene=gene_name).first()
    gene_lof = RareMac3SaigeLof.query.filter_by(gene=gene_name).first()
    if gene_damage is not None:
        data[''] = dict(gene_damage)
    if gene_lof is not None:
        data['lof'] = dict(gene_lof)
    if gene_lof is None and gene_damage is None:
        return NoDataError(chinese_msg='没有相应的数据')
    return data
