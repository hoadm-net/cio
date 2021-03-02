from helpers import vncorenlp_pos_tag, sentiment_mapper, emphasize_sentiment


def sentiment_analysis_facade(sentence):
    tagged = vncorenlp_pos_tag(sentence)
    sentiment_mapped = []
    for word in tagged:
        sentiment_mapped.append(sentiment_mapper(word))

    result = list()
    for idx, word in enumerate(sentiment_mapped):
        if word['sentiment'] != 'none':
            if idx == 0:
                pre_w = None
            else:
                pre_w = sentiment_mapped[idx - 1]

            if idx == (len(sentiment_mapped) - 1):
                nxt_w = None
            else:
                nxt_w = sentiment_mapped[idx + 1]

            new_w = emphasize_sentiment(word, pre_w, nxt_w)
            result.append(new_w)
        else:
            result.append(word)

    return result
