
#urls.py

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.jwtToken, name='jwtToken'),
    path('cus/', views.CustomerList.as_view()),
    path('cus/<int:pk>/', views.CustomerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
