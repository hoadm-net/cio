from django.db import models


class AdverbLVL:
    Intensifier = 1
    Booster = 2
    Diminisher = 3
    Minimizer = 4
    Modifier = 5
    Negative = 100


class WordSentiment:
    Negative = 1
    Positive = 2


class Adverb(models.Model):
    ADVERB_LEVELS = (
        (1, 'Intensifier'),
        (2, 'Booster'),
        (3, 'Diminisher'),
        (4, 'Minimizer'),
        (5, 'Modifier'),
        (100, 'Negative')
    )

    txt = models.CharField(max_length=100, verbose_name='Text', unique=True)
    lvl = models.SmallIntegerField(choices=ADVERB_LEVELS, verbose_name='Level')

    def __str__(self):
        return self.txt

    def __repr__(self):
        return self.txt

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.txt = self.txt.lower().strip().replace(' ', '_')
        super(Adverb, self).save(force_insert, force_update, using, update_fields)


class Word(models.Model):
    WORD_SENTIMENTS = (
        (1, 'Negative'),
        (2, 'Positive')
    )

    txt = models.CharField(max_length=100, verbose_name='Text', unique=True)
    score = models.FloatField(verbose_name='Score')
    sentiment = models.SmallIntegerField(choices=WORD_SENTIMENTS, verbose_name='Sentiment')

    def __str__(self):
        return self.txt

    def __repr__(self):
        return self.txt

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.txt = self.txt.lower().strip().replace(' ', '_')
        super(Word, self).save(force_insert, force_update, using, update_fields)
