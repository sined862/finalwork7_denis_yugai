from django.shortcuts import render
from guestbook.models import Guest
from guestbook.forms import SearchForm
from guestbook.forms import GuestForm

def index_view(request):
    form_finder = SearchForm()
    form = GuestForm()
    if request.method == 'GET':
        if not request.GET.get('author'):
            guests = Guest.objects.filter(status='active').order_by('created_at').reverse
            context = {
                'guests': guests,
                'form': form,
                'form_finder': form_finder
            }
            return render(request, 'index.html', context)
        else:
            guests = Guest.objects.filter(author_name=request.GET.get('author')).order_by('created_at').reverse
            error = 'Ни одной записи не найдено'
            context = {
                'guests': guests,
                'error': error,
                'form_finder': form_finder,
                'form': form
            }
            return render(request, 'index.html', context)
        
        