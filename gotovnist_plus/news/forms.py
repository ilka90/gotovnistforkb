from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Навза статті'

            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статті'

            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статті'

            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'

            })
            

        }