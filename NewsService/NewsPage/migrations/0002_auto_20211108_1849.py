# Generated by Django 3.2.9 on 2021-11-08 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleabstract',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='CategoryAbstract',
        ),
    ]
