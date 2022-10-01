from django.contrib import admin
from guestbook.models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author_name', 
        'author_email', 
        'created_at',
        'changed_at',
        'status'
    )
    list_filter = (
        'id',
        'author_name', 
        'author_email',
        'textrec', 
        'created_at',
        'changed_at',
        'status'
    )
    search_fields = (
        'author_name', 
        'author_email', 
        'textrec',
        'created_at',
        'changed_at',
        'status'
    )
    fields = (
        'author_name', 
        'author_email', 
        'textrec',
        'status'
    )

admin.site.register(Guest, GuestAdmin)




