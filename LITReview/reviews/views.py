from itertools import chain
from .models import UserFollows
from .forms import TicketForm, ReviewForm, SubscriptionForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


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

@login_required
def subscriptions(request):
    user_follows = UserFollows.objects.filter(user_id=request.user.id)
    user_followed_by = UserFollows.objects.filter(followed_user_id=request.user.id)
    
    if request.method != 'POST':
        form = SubscriptionForm()
    else:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            user_follow = form.save(commit=False)
            user_follow.user = request.user
            try:
                user_follow.save()
            except IntegrityError:
                print("Vous êtes déjà abonné à cet utilisateur")

    context = {'form': form, 'users_follows':user_follows, 'user_followed_by': user_followed_by}
    return render(request, 'reviews/subscriptions.html', context)
    
@login_required
def delete_subscription(request, id):
    subscription = UserFollows.objects.get(pk=id)
    subscription.delete()
    return redirect('/reviews/subscriptions/')
