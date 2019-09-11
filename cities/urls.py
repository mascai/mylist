# cities/urls.py
from django.urls import path
from . import views
from .views import HomePageView, SearchResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('city/<int:pk>/', views.city_detail, name='city_detail'),
]
