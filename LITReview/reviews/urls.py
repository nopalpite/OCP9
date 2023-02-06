from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('feeds/', views.feeds, name='feeds'),
    path('posts/', views.posts, name='posts'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('create_ticket_and_review/', views.create_ticket_and_review,
         name='create_ticket_and_review'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('delete_subscription/<id>/',
         views.delete_subscription, name='delete_subscription'),
    path('create_review/<id>/', views.create_review, name='create_review'),
    path('update_review/<id>/', views.update_review, name='update_review'),
    path('delete_review/<id>/', views.delete_review, name='delete_review'),
    path('update_ticket/<id>/', views.update_ticket, name='update_ticket'),
    path('delete_ticket/<id>/', views.delete_ticket, name='delete_ticket'),
]
