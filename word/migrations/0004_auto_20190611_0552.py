# Generated by Django 2.2.2 on 2019-06-11 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0003_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='sentiment',
            field=models.SmallIntegerField(choices=[(1, 'Negative'), (2, 'Positive')], verbose_name='Sentiment'),
        ),
    ]