from django import forms

from .models import User

# from .models import Ticket

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'ticket')

# class TicketForm(forms.ModelForm):
#     class Meta:
#         model = Ticket
#         fields = ('number')
