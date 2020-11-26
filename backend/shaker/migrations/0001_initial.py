# Generated by Django 3.1.1 on 2020-11-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('intitule', models.CharField(db_column='INTITULE', max_length=255)),
                ('illustrationurl', models.CharField(blank=True, db_column='ILLUSTRATIONURL', max_length=255, null=True)),
                ('categorie', models.CharField(db_column='CATEGORIE', max_length=255)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('forcealc', models.IntegerField(blank=True, db_column='FORCEALC', null=True)),
            ],
            options={
                'db_table': 'COCKTAIL',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contenir',
            fields=[
                ('idcontenir', models.IntegerField(db_column='IDCONTENIR', primary_key=True, serialize=False)),
                ('quantite', models.IntegerField(db_column='QUANTITE')),
                ('unite', models.CharField(blank=True, db_column='UNITE', max_length=16, null=True)),
            ],
            options={
                'db_table': 'CONTENIR',
                'managed': False,
            },
        ),
    ]
