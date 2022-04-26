from django.urls import path
from app_rss.feeds import LatestHouse

urlpatterns=[
    path('latest/feed/',LatestHouse(), name='rss')
]