from word.models import Word
from django.core.exceptions import ObjectDoesNotExist


def sentiment_mapper(w):
    """
    Kiểm tra 1 từ có được đặc tể về tình cảm (có tồn tại trong Lexicon).
    *) Chú ý: bỏ qua trạng từ. Trong trường hợp này trạng từ chỉ nhằm mục đích bổ trợ cho tính từ.
    """
    if w['type'] == 'R':
        w['sentiment'] = 'none'
        w['score'] = 0
    else:
        try:
            res = Word.objects.get(txt__exact=w['txt'])
            w['sentiment'] = res.sentiment
            w['score'] = res.score
        except ObjectDoesNotExist:
            w['sentiment'] = 'none'
            w['score'] = 0

    return w
