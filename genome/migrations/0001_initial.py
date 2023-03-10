# Generated by Django 3.2.12 on 2022-03-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study', models.CharField(max_length=32)),
                ('tissue_cell', models.CharField(max_length=32)),
                ('gene_name', models.CharField(max_length=32)),
                ('gene_symbol', models.CharField(max_length=32)),
                ('credible_set', models.PositiveSmallIntegerField()),
                ('snp', models.CharField(max_length=128)),
                ('rs_id', models.CharField(max_length=32)),
                ('vaf', models.FloatField()),
                ('m_log', models.FloatField()),
                ('effect_size', models.FloatField()),
                ('se', models.FloatField()),
                ('pip', models.FloatField()),
            ],
        ),
    ]
