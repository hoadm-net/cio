from django.views import View
from django.shortcuts import render
from helpers import full_analyze


class HomeView(View):
    template = 'frontend/index.html'

    def get(self, request):
        return render(
            request,
            self.template
        )


class ABSAView(View):
    """
    Aspect-Based Sentiment Analysis
    """
    template = 'frontend/absa.html'

    def get(self, request):

        return render(
            request,
            self.template
        )
