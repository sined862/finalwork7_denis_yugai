from django.urls import path
from guestbook.views.base import index_view
from guestbook.views.guests import add_view, update_view


urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view, name='guest_add'),
    path('update/<int:pk>', update_view, name='guest_update')
]