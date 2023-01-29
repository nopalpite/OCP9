from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('feeds/', views.feeds, name='feeds'),
    path('posts/', views.posts, name='posts'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('create_ticket_and_review/', views.create_ticket_and_review, name='create_ticket_and_review'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('delete_subscription/<id>/', views.delete_subscription, name='delete_subscription'),
    path('create_review/<id>/', views.create_review, name='create_review'),
]
 
