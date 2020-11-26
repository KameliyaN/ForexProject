from django.urls import path, include

from currencies import views

urlpatterns = [
    path('add_currency/', views.CurrencyCreateView.as_view(), name='add currency'),
    path('edit_currency/<int:pk>/', views.CurrencyUpdateView.as_view(), name='edit currency'),
    path('all_currency/', views.CurrencyAllView.as_view(), name='all_currency'),
    path('detail_currency/<int:pk>/', views.CurrencyDetailView.as_view(), name='detail currency'),
    path('delete_currency/<int:pk>/', views.CurrencyDeleteView.as_view(), name='delete currency'),
    path('live_quotes/', views.currencies_live_quotes, name='live quotes'),
    path('add_category/', views.CategoryCreateView.as_view(), name='add category'),
    path('add_links/', views.LinkCreateView.as_view(), name='add links'),
    path('all_links/', views.LinkAllView.as_view(), name='all links'),
]
