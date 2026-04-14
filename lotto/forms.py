from django import forms
from .models import DrawComment


class DrawCommentForm(forms.ModelForm):
    class Meta:
        model = DrawComment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment about this draw...'
            })
        }


class SubscriptionJoinForm(forms.Form):
    confirm_join = forms.BooleanField(
        required=True,
        label='I understand I will be charged for the remaining draws in this month.'
    )
