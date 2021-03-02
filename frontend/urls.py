from django.urls import re_path, path
from .views import HomeView, ABSAView

urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    path('phan-tich-tinh-cam-dua-tren-khia-canh', ABSAView.as_view(), name='ABSA')
]
