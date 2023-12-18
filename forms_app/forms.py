from django import forms

from forms_app.models import Message


class ContactForm(forms.Form):
    CHOICES = [
        ("", "--------"),
        ("question", "Pytanie"),
        ("other", "Inne")
    ]

    name = forms.CharField(label="Imię")
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(label="Kategoria", choices=CHOICES)
    subject = forms.CharField(label="Tytuł")
    body = forms.CharField(label="Treść", widget=forms.Textarea())
    date = forms.DateField(label="Ulubiona data", widget=forms.NumberInput(attrs={"type": "date"}))
    time = forms.TimeField(label="Ulubiona godzina", widget=forms.NumberInput(attrs={"type": "time"}))


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        # fields = [
        #     'name',
        #     'email',
        #     'category',
        #     'subject',
        #     'body',
        #     'date',
        #     'time'
        # ]

        labels = {
            "name": "Imię",
            "email": "Email",
            "category": "Kategoria",
            "subject": "Tytuł",
            "body": "Treść",
            "date": "Ulubiona data",
            "time": "Ulubiony czas"
        }

        widgets = {
            "date": forms.NumberInput(attrs={"type": "date"}),
            "time": forms.NumberInput(attrs={"type": "time"})
        }
