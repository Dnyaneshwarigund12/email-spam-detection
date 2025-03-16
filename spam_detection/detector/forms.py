from django import forms


class MessageForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control scrollbar",
                "id": "style-7",
                "placeholder": "Enter your message here...",
            }
        )
    )
