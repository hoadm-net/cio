# Generated by Django 2.2.2 on 2019-06-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adverb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.CharField(max_length=100)),
                ('lvl', models.SmallIntegerField(choices=[(1, 'Intensifier'), (2, 'Booster'), (3, 'Diminisher'), (4, 'Minimizer'), (5, 'Modifier')])),
            ],
        ),
    ]
