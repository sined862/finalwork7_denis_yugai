from django.urls import path
from guestbook.views.base import index_view
from guestbook.views.guests import add_view, update_view
from guestbook.views.guests import del_view, del_view, del_confirm_view


urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view, name='guest_add'),
    path('update/<int:pk>', update_view, name='guest_update'),
    path('del/<int:pk>', del_view, name='guest_del'),
    path('del_confirm/<int:pk>', del_confirm_view, name='guest_del_confirm'),
    path('search/', index_view, name='search')
]