from itertools import chain

from .forms import TicketForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def feeds(request):
    
    
    return render(request, 'reviews/feeds.html')

@login_required
def create_ticket(request):
    if request.method != 'POST':
        form = TicketForm()
    else:
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('/reviews/feeds/')

    context = {'form': form}
    return render(request, 'reviews/create_ticket.html', context)

        