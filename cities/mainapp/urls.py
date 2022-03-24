from django.urls import path
from .views import HomePage, CityDetail


urlpatterns = [
    path('city/<slug:slug>/', CityDetail.as_view(), name='city'),
    path('', HomePage.as_view(), name='homepage'),
]
