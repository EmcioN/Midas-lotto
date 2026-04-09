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
    full_month_price = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        min_value=0
    )
