from django.urls import path
from core.views import fetch_videos

urlpatterns = [
    path('list/<int:page>/', fetch_videos),
]