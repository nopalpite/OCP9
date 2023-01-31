from itertools import chain

from .models import UserFollows, Review, Ticket
from .forms import TicketForm, ReviewForm, SubscriptionForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import CharField, Value

@login_required
def feeds(request):
    user_follows = UserFollows.objects.filter(user_id=request.user.id).values('followed_user')
    reviews = Review.objects.filter(user_id__in=user_follows) | Review.objects.filter(user_id=request.user.id)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = Ticket.objects.filter(user_id__in=user_follows) | Ticket.objects.filter(user_id=request.user.id)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created, 
        reverse=True
    )
    user_reviews = Review.objects.filter(user_id=request.user.id)
    tickets_reviewed = []
    for review in user_reviews:
        if review.ticket in tickets:
            tickets_reviewed.append(review.ticket)
    return render(request, 'reviews/feeds.html', context={'posts': posts, 'tickets_reviewed': tickets_reviewed})

@login_required
def posts(request):
    reviews = Review.objects.filter(user=request.user.id)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = Ticket.objects.filter(user=request.user.id)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created, 
        reverse=True
    )
    return render(request, 'reviews/posts.html', context={'posts': posts})

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
def create_review(request, id):
    ticket = Ticket.objects.get(pk=id)
    if request.method != 'POST':
        review_form = ReviewForm()
    else:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('/reviews/feeds/')
    context = {'review_form': review_form, 'ticket': ticket}
    return render(request, 'reviews/create_review.html', context)


@login_required
def update_review(request, id):
    review = Review.objects.get(pk=id)
    if review.user == request.user:
        if request.method != 'POST':
            review_form = ReviewForm(instance=review)
        else:
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review = review_form.save()
                review.save()
                return redirect('/reviews/posts/')
        context = {'review_form': review_form, 'ticket': review.ticket}
    else:
        print("vous n'avez pas le droit de faire ça")
        context = {}
        return redirect('/reviews/posts/')
    
    return render(request, 'reviews/update_review.html', context)

@login_required
def delete_review(request, id):
    review = Review.objects.get(pk=id)
    if review.user == request.user:
        review.delete()
        print("review supprimée")
    else:
        print("vous n'avez pas le droit de faire ça")
    return redirect('/reviews/posts/')

@login_required
def update_ticket(request, id):
    ticket = Ticket.objects.get(pk=id)
    if ticket.user == request.user:
        if request.method != 'POST':
            ticket_form = TicketForm(instance=ticket)
        else:
            ticket_form = TicketForm(request.POST, request.FILES, instance=ticket)
            if ticket_form.is_valid():
                ticket = ticket_form.save()
                ticket.save()
                return redirect('/reviews/posts/')
        context = {'form': ticket_form }
    else:
        print("vous n'avez pas le droit de faire ça")
        context = {}
        return redirect('/reviews/posts/')
    
    return render(request, 'reviews/update_ticket.html', context)

@login_required
def delete_ticket(request, id):
    ticket = Ticket.objects.get(pk=id)
    if ticket.user == request.user:
        ticket.delete()
        print("ticket supprimé")
    else:
        print("vous n'avez pas le droit de faire ça")
    return redirect('/reviews/posts/')

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
    if subscription.user == request.user:
        subscription.delete()
        print("abonnement supprimé")
    else:
        print("vous n'avez pas le droit de faire ça")
    return redirect('/reviews/subscriptions/')
