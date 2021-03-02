import math
from word.models import Adverb, AdverbLVL, WordSentiment
from django.core.exceptions import ObjectDoesNotExist


def adv_classifier(adv):
    try:
        adv = Adverb.objects.get(txt__exact=adv['txt'])
        return adv.lvl
    except ObjectDoesNotExist:
        return None


def adv_norm(adv, word):
    original_score = float(word['score'])
    abs_score = math.fabs(original_score)
    lvl_adv = adv_classifier(adv)
    if lvl_adv == AdverbLVL.Intensifier:
        score = 1 - math.pow((1 - abs_score), 4)
    elif lvl_adv == AdverbLVL.Booster:
        score = 1 - math.pow((1 - abs_score), 2)
    elif lvl_adv == AdverbLVL.Diminisher:
        score = 1 - math.pow((1 - abs_score), 0.5)
    elif lvl_adv == AdverbLVL.Minimizer:
        score = 1 - math.pow((1 - abs_score), 0.25)
    elif lvl_adv == AdverbLVL.Negative:
        score = (-1) * abs_score
    else:
        score = original_score

    if word['sentiment'] == WordSentiment.Negative:
        score = score * (-1)

    if score != original_score:
        word['original_score'] = original_score
        word['score'] = score
        word['adv'] = adv['txt']

    return word


def adv_after_adj(adv, word):
    original_score = float(word['score'])
    abs_score = math.fabs(original_score)
    lvl_adv = adv_classifier(adv)

    expr_1 = 1 - math.pow((1 - abs_score), 4)
    expr_2 = 1 - math.pow((1 - abs_score), 2)
    expr_3 = 1 - math.pow((1 - abs_score), 0.5)
    expr_4 = 1 - math.pow((1 - abs_score), 0.25)

    if lvl_adv == AdverbLVL.Intensifier:
        score = (expr_1 + 1) / 2
    elif lvl_adv == AdverbLVL.Booster:
        score = (expr_1 + expr_2) / 2
    elif lvl_adv == AdverbLVL.Diminisher:
        score = (expr_2 + expr_3) / 2
    elif lvl_adv == AdverbLVL.Minimizer:
        score = (expr_3 + expr_4) / 2
    elif lvl_adv == AdverbLVL.Negative:
        score = (-1) * abs_score
    else:
        score = original_score

    if word['sentiment'] == WordSentiment.Negative:
        score = score * (-1)

    if score != original_score:
        word['original_score'] = original_score
        word['score'] = score
        word['adv'] = adv['txt']

    return word


def emphasize_sentiment(word, pre_w=None, nxt_w=None):
    # adj - adv
    if word['type'] == 'A' and nxt_w is not None and nxt_w['type'] == 'R':
        return adv_after_adj(nxt_w, word)

    # adv - adj/v
    if nxt_w is not None and nxt_w['type'] == 'R':
        return adv_norm(nxt_w, word)

    if pre_w is not None and pre_w['type'] == 'R':
        return adv_norm(pre_w, word)

    return word


def simple_emphasize_sentiment(sent, word_idx, adv_idx):
    word = sent[word_idx]
    adv = sent[adv_idx]

    original_score = float(word['score'])
    abs_score = math.fabs(original_score)
    lvl_adv = adv_classifier(adv)

    expr_1 = 1 - math.pow((1 - abs_score), 4)
    expr_2 = 1 - math.pow((1 - abs_score), 2)
    expr_3 = 1 - math.pow((1 - abs_score), 0.5)
    expr_4 = 1 - math.pow((1 - abs_score), 0.25)

    if adv_idx > word_idx and word['type'] == 'A':
        if lvl_adv == AdverbLVL.Intensifier:
            score = (expr_1 + 1) / 2
        elif lvl_adv == AdverbLVL.Booster:
            score = (expr_1 + expr_2) / 2
        elif lvl_adv == AdverbLVL.Diminisher:
            score = (expr_2 + expr_3) / 2
        elif lvl_adv == AdverbLVL.Minimizer:
            score = (expr_3 + expr_4) / 2
        elif lvl_adv == AdverbLVL.Negative:
            score = (-1) * abs_score
        else:
            score = abs_score

        if word['sentiment'] == WordSentiment.Negative:
            score = score * (-1)

        if score != original_score:
            word['original_score'] = original_score
            word['score'] = score
    else:
        if lvl_adv == AdverbLVL.Intensifier:
            score = expr_1
        elif lvl_adv == AdverbLVL.Booster:
            score = expr_2
        elif lvl_adv == AdverbLVL.Diminisher:
            score = expr_3
        elif lvl_adv == AdverbLVL.Minimizer:
            score = expr_4
        elif lvl_adv == AdverbLVL.Negative:
            score = (-1) * abs_score
        else:
            score = abs_score

        if word['sentiment'] == WordSentiment.Negative:
            score = score * (-1)

        if score != original_score:
            word['original_score'] = original_score
            word['score'] = score
