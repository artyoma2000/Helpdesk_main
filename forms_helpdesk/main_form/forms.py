from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['Recipient', 'Service', 'Location', 'Office', 'Floor', 'Building', 'Topic', 'Main_text', 'priority']

        widgets = {
            'Recipient': TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО получателя'}),
            'Service': Select(attrs={'class': 'form-control', 'placeholder': 'Сервис'}),
            'Location': Select(attrs={'class': 'form-control', 'placeholder': 'Расположение'}),
            'Office': TextInput(attrs={'class': 'form-control', 'placeholder': 'Кабинет'}),
            'Floor': TextInput(attrs={'class': 'form-control', 'placeholder': 'Этаж'}),
            'Building': TextInput(attrs={'class': 'form-control', 'placeholder': 'Корпус'}),
            'Topic': TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема'}),
            'Main_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Опишите проблему'}),
            'priority': Select(attrs={'class': 'form-control', 'placeholder': 'Приоритет'})


        }
