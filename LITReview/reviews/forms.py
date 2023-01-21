from .models import Ticket, Review, UserFollows
from bootstrap5.widgets import RadioSelectButtonGroup

from django.forms import ModelForm
    


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

class ReviewForm(ModelForm):
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