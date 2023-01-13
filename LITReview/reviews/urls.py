from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('feeds/', views.feeds, name='feeds'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    # path('create_review/', views.create_review, name='create_review'),
    # path('create_ticket_and_review/', views.create_ticket_and_review, name='create_ticket_and_review'),
]
 
