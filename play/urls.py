from django.urls import path

from . import views


urlpatterns = [
    path('<int:song_id>/', views.playView, name = 'play'),
    path('download/<int:song_id>/', views.downloadView, name = 'download'),
]