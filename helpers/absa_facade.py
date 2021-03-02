from helpers import full_analyze
from helpers.feature_extraction import FeatureExtraction


def absa_facade(paragraph):
    result = dict()
    analyzed_data = []
    sentences = paragraph.strip().lower().split('.')
    raw_sentences = []
    for sent in sentences:
        if len(sent) > 0:
            sent += '.'
            analyzed_data.append(full_analyze(sent))
            raw_sentences.append(sent)

    result['raw_data'] = analyzed_data
    result['sentences'] = raw_sentences
    result['features'] = FeatureExtraction(analyzed_data)()
    return result
