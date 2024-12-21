from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/add/', views.artist_add, name='artist_add'),  # Добавить художника
    path('artists/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('artists/<int:pk>/edit/', views.artist_edit, name='artist_edit'),
    path('artists/<int:pk>/delete/', views.artist_delete, name='artist_delete'),

    path('museums/', views.museum_list, name='museum_list'),
    path('museums/add/', views.museum_add, name='museum_add'),  # Добавить музей
    path('museums/<int:pk>/', views.museum_detail, name='museum_detail'),
    path('museums/<int:pk>/edit/', views.museum_edit, name='museum_edit'),
    path('museums/<int:pk>/delete/', views.museum_delete, name='museum_delete'),

    path('paintings/', views.painting_list, name='painting_list'),
    path('paintings/add/', views.painting_add, name='painting_add'),  # Добавить картину
    path('paintings/<int:pk>/', views.painting_detail, name='painting_detail'),
    path('paintings/<int:pk>/edit/', views.painting_edit, name='painting_edit'),
    path('paintings/<int:pk>/delete/', views.painting_delete, name='painting_delete'),
]
