from django.db import models


class Row(models.Model):
    study = models.CharField(max_length=32)
    tissue_cell = models.CharField(max_length=32)
    gene_name = models.CharField(max_length=32)
    gene_symbol = models.CharField(max_length=32)
    credible_set = models.PositiveSmallIntegerField()
    snp = models.CharField(max_length=128)
    rs_id = models.CharField(max_length=32)
    vaf = models.FloatField()
    m_log = models.FloatField()
    effect_size = models.FloatField()
    se = models.FloatField()
    pip = models.FloatField()
