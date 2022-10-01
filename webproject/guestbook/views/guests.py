from django.shortcuts import render, redirect, get_object_or_404
from guestbook.models import Guest
from guestbook.forms import GuestForm


def add_view(request):
    form = GuestForm()
    if request.method == 'GET':
        context = {'form': form}
        return render(request, 'guest_create.html', context)
    form = GuestForm(request.POST)
    if not form.is_valid():
        context = {'form': form}
        return render(request, 'guest_create.html', context)
    guest = Guest.objects.create(**form.cleaned_data)
    return redirect('index')


def update_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'GET':
        form = GuestForm(initial={
            'author_name': guest.author_name,
            'author_email': guest.author_email,
            'textrec': guest.textrec
        })
        return render(request, 'guest_update.html', context={'form':form, 'guest': guest})
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest.author_name = form.cleaned_data['author_name']
            guest.author_email = form.cleaned_data['author_email']
            guest.textrec = form.cleaned_data['textrec']
            guest.save()
            return redirect('index')
        else:
            return render(request, 'guest_update.html', context={'form': form, 'guest': guest})


def del_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    context = {'guest': guest}
    return render(request, 'confirm_delete.html', context)

def del_confirm_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    guest.delete()
    return redirect('index')
            
