# Generated by Django 2.0.6 on 2021-10-31 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'カテゴリ', 'verbose_name_plural': 'カテゴリ'},
        ),
        migrations.AlterModelOptions(
            name='kakeibo',
            options={'verbose_name': '家計簿', 'verbose_name_plural': '家計簿'},
        ),
    ]
