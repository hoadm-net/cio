from vncorenlp import VnCoreNLP


"""
------------------------------------
Clausal Argument Relations Description
------------------------------------
NSUBJ Nominal subject
DOBJ Direct object
IOBJ Indirect object
CCOMP Clausal complement
XCOMP Open clausal complement
------------------------------------
Nominal Modifier Relations Description
------------------------------------
NMOD Nominal modifier
AMOD Adjectival modifier
NUMMOD Numeric modifier
APPOS Appositional modifier
DET Determiner
CASE Prepositions, postpositions and other case markers
------------------------------------
Other Notable Relations Description
------------------------------------
CONJ Conjunct
CC Coordinating conjunction
"""


def vncorenlp_dep_parse(paragraph):
    with VnCoreNLP(address='http://127.0.0.1', port=8888) as vn_core_nlp:
        tagged = vn_core_nlp.pos_tag(paragraph)
        parsed = vn_core_nlp.dep_parse(paragraph)

    result = []
    tokens = tagged[0]
    parsed = parsed[0]
    for idx, token in enumerate(tokens):
        w = {
            'txt':  token[0],
            'type': token[1],
            'kind': parsed[idx][0],
            'dependence': parsed[idx][1]
        }
        result.append(w)
    return result
