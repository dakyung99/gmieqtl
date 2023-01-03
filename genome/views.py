import csv
from collections import OrderedDict

from django.http import HttpResponse
from django.shortcuts import render

from genome.models import Row


def index(request):
    FIELD_CHOICES = [
        ('study', 'study'),
        ('Tissue/Cell', 'tissue_cell'),
        ('GeneName', 'gene_name'),
        ('GeneSymbol', 'gene_symbol'),
        ('CREDIBLE_SET', 'credible_set'),
        ('SNP', 'snp'),
        ('rsID', 'rs_id'),
        ('VAF', 'vaf'),
        ('mLOG(P)', 'm_log'),
        ('EffectSize', 'effect_size'),
        ('SE', 'se'),
        ('PIP', 'pip')
    ]

    row_set = Row.objects.all()

    # 검색
    keyword = request.GET.get('keyword', '')
    if keyword:
        row_set = row_set.filter(gene_symbol__icontains=keyword)

    # 정렬
    o_type = request.GET.get('o_type', 'study')
    o_reverse = 'o_reverse' in request.GET
    row_set = row_set.order_by(o_type if not o_reverse else '-{}'.format(o_type))

    # CSV 다운로드
    if 'download' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response.write(u'\ufeff'.encode('utf8'))
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        dw = csv.DictWriter(
            response,
            delimiter=',',
            quotechar='"',
            fieldnames=OrderedDict(map(lambda choice: (choice[0], None), FIELD_CHOICES))
        )
        dw.writeheader()
        for row in row_set:
            dw.writerow(dict(map(lambda choice: (choice[0], getattr(row, choice[1])), FIELD_CHOICES)))

        return response

    context = {
        'row_set': row_set,
        'keyword': keyword,
        'o_type': o_type,
        'o_reverse': o_reverse,
        'FIELD_CHOICES': FIELD_CHOICES
    }
    return render(request, 'index.html', context)
