from django.shortcuts import render
from guestbook.models import Guest

def index_view(request):
    guests = Guest.objects.filter(status='active').order_by('created_at').reverse
    context = {
        'guests': guests
    }
    return render(request, 'index.html', context)