from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['Recipient', 'Service', 'Location', 'Office', 'Floor', 'Building', 'Topic', 'Main_text', 'priority']

        widgets = {
            'Recipient': TextInput(attrs={'placeholder': 'ФИО получателя'}),
            'Service': Select(attrs={'placeholder': 'Сервис'}),
            'Location': Select(attrs={'placeholder': 'Расположение'}),
            'Office': TextInput(attrs={'placeholder': 'Кабинет'}),
            'Floor': TextInput(attrs={'placeholder': 'Этаж'}),
            'Building': TextInput(attrs={'placeholder': 'Корпус'}),
            'Topic': TextInput(attrs={'placeholder': 'Тема'}),
            'Main_text': Textarea(attrs={'placeholder': 'Опишите проблему'}),
            'priority': Select(attrs={'placeholder': 'Приоритет'})


        }
