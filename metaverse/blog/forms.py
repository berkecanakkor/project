from django.forms import ModelForm, TextInput,Textarea
from blog.models import contactFormModel

class ContactForm(ModelForm):
    class Meta:
        model = contactFormModel
        fields = ['username', 'message']
        widgets = {
            'username': TextInput(attrs={'class': 'input'}),
            'message': Textarea(attrs={'class': 'textarea'})
        }


