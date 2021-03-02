# Generated by Django 2.2.2 on 2019-06-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0004_auto_20190611_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adverb',
            name='lvl',
            field=models.SmallIntegerField(choices=[(1, 'Intensifier'), (2, 'Booster'), (3, 'Diminisher'), (4, 'Minimizer'), (5, 'Modifier'), (100, 'Negative')], verbose_name='Level'),
        ),
    ]