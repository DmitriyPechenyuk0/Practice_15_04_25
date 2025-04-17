from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(
        max_length = 100,
        widget = forms.TextInput(
            attrs = {"placeholder": "Задайте Ваше ім'я"}
        )
    )
    email = forms.EmailField(
        widget = forms.TextInput(
            attrs = {"placeholder": "Задайте Вашу електронну адресу"}
        )
    )
    message = forms.CharField(
        widget = forms.Textarea(
            attrs = {"placeholder": "Напишіть відгук"}
        )
    )