from django.urls import path
from guestbook.views.base import index_view


urlpatterns = [
    path('', index_view, name='index')
]