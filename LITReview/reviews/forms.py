from .models import Ticket, Review, UserFollows
from bootstrap5.widgets import RadioSelectButtonGroup
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm
from django import forms

CHOICES =(
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)
      


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

class ReviewForm(ModelForm):
    rating = forms.ChoiceField(choices=CHOICES, widget=RadioSelectButtonGroup)
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        labels = {
            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Commentaire'
        }
        

class SubscriptionForm(ModelForm):
    class Meta:
        model = UserFollows
        fields = ['followed_user']
        labels = {
            'followed_user': "Nom d'utilisateur"
        }
        