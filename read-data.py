import csv
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from genome.models import Row

csv_file = open('data.csv', encoding='utf-8-sig', mode='r')
csv_lines = csv.DictReader(csv_file.read().splitlines(), delimiter=',', quotechar='"')

rows_to_create = []
for csv_line in csv_lines:
    rows_to_create.append(
        Row(
            study=csv_line['study'],
            tissue_cell=csv_line['Tissue/Cell'],
            gene_name=csv_line['GeneName'],
            gene_symbol=csv_line['GeneSymbol'],
            credible_set=int(csv_line['CREDIBLE_SET']),
            snp=csv_line['SNP'],
            rs_id=csv_line['rsID'],
            vaf=float(csv_line['VAF']),
            m_log=float(csv_line['mLOG(P)']),
            effect_size=float(csv_line['EfffectSize']),
            se=float(csv_line['SE']),
            pip=float(csv_line['PIP'])
        )
    )

Row.objects.bulk_create(rows_to_create)
