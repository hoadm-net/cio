import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from helpers import sentiment_analysis_facade, absa_facade


def normalize_data(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    input_data = body['input_data'].strip().lower()
    return input_data


@require_POST
def sentiment_analyze(request):
    input_data = normalize_data(request)
    result = sentiment_analysis_facade(input_data)
    data = {
        'analyzed_data': result
    }
    return JsonResponse(data)


@require_POST
def dependency_parsing(request):
    input_data = normalize_data(request)
    result = absa_facade(input_data)

    data = result

    return JsonResponse(data)
