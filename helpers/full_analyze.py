from vncorenlp import VnCoreNLP
from helpers import sentiment_mapper, simple_emphasize_sentiment


def full_analyze(sentence):
    result = list()
    with VnCoreNLP(address='http://127.0.0.1', port=8888) as vn_core_nlp:
        tagged = vn_core_nlp.pos_tag(sentence)[0]
        dep_parsed = vn_core_nlp.dep_parse(sentence)[0]

    for idx, word in enumerate(tagged):
        parsed_word = dict()
        parsed_word['txt'] = tagged[idx][0]
        parsed_word['type'] = tagged[idx][1]
        parsed_word['kind'] = dep_parsed[idx][0]
        parsed_word['mod'] = list()
        parsed_word['conj'] = list()

        if dep_parsed[idx][1] > 0:
            parsed_word['depend_on'] = dep_parsed[idx][1] - 1
        else:
            parsed_word['depend_on'] = None
        parsed_word['dependencies'] = list()

        for i, w in enumerate(dep_parsed):
            if (dep_parsed[i][1] - 1) == idx:
                parsed_word['dependencies'].append(i)

        result.append(parsed_word)

    # apply sentiment
    for word in result:
        sentiment_mapper(word)

    # find mod word and emphasize
    for wid, word in enumerate(result):
        if len(word['dependencies']) > 0:
            for dep_idx in word['dependencies']:
                if word['type'] == 'A' and (result[dep_idx]['kind'] == 'amod' or result[dep_idx]['kind'] == 'adv'):
                    word['mod'].append(dep_idx)
                    simple_emphasize_sentiment(result, wid, dep_idx)
                elif word['type'] == 'V' and (result[dep_idx]['kind'] == 'vmod' or result[dep_idx]['kind'] == 'adv'):
                    word['mod'].append(dep_idx)
                    simple_emphasize_sentiment(result, wid, dep_idx)
                elif word['type'] == 'N' and result[dep_idx]['kind'] == 'nmod':
                    word['mod'].append(dep_idx)
                elif word['type'] == 'P' and result[dep_idx]['kind'] == 'pmod':
                    word['mod'].append(dep_idx)

    # find conjunctions
    # print(result)
    for word in result:
        if word['kind'] == 'coord':
            first = None
            second = None
            if word['depend_on'] is not None:
                first = word['depend_on']

            if len(word['dependencies']) > 0:
                second = word['dependencies'][0]

            if first is not None and second is not None:
                result[first]['conj'].append(second)
                result[second]['conj'].append(first)

    return result
