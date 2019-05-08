from django.conf.urls import url
from django.urls import path

from music.views import ListSongsView
from .import views

urlpatterns = [

    path('songs/', ListSongsView.as_view(), name="songs")

]