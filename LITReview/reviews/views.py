from itertools import chain

from .forms import TicketForm, ReviewForm
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

@login_required
def create_ticket_and_review(request):
    if request.method != 'POST':
        ticket_form = TicketForm()
        review_form = ReviewForm()
    else:
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('/reviews/feeds/')

    context = {'ticket_form': ticket_form,'review_form': review_form}
    return render(request, 'reviews/create_ticket_and_review.html', context)

