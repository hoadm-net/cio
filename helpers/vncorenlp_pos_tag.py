from vncorenlp import VnCoreNLP


def vncorenlp_pos_tag(sentence):
    with VnCoreNLP(address='http://127.0.0.1', port=8888) as vn_core_nlp:
        tagged = vn_core_nlp.pos_tag(sentence)

    result = list()
    fs_tagged = tagged[0]

    for w in fs_tagged:
        parsed_w = {
            'txt': w[0],
            'type': w[1]
        }

        result.append(parsed_w)

    return result
