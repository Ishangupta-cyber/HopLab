from django.urls import path
from .views import RecentLinksView, ShortenView, redirect_view

urlpatterns = [
    path("api/shorten/", ShortenView.as_view()),
    path("api/links/", RecentLinksView.as_view()),
    path("<str:code>", redirect_view),     
]