from django.db import models


# Create your models here.
class Articles(models.Model):

    Service_TYPES= [
        ('ИТ Отдел', 'ИТ Отдел'),

    ]
    Location_TYPES= [
        ('Авиационный переулок', 'Авиационный переулок'),
        ('Кавказский бульвар', 'Кавказский бульвар'),
        ('Электрический переулок', 'Электрический переулок')

    ]

    priority_TYPES= [
        ('Низкий', 'Низкий'),
        ('Нормальный', 'Нормальный'),
        ('Высокий', 'Высокий')

    ]

    Recipient = models.TextField('ФИО получателя', max_length=50, default='')
    Service = models.CharField('Сервис', max_length=50, choices=Service_TYPES)
    Location = models.CharField('Расположение', max_length=250, choices=Location_TYPES)
    Office = models.TextField('Кабинет', max_length=50, default='')
    Floor = models.TextField('Этаж', max_length=50, default='')
    Building = models.TextField('Корпус', max_length=50, default='')
    Topic = models.TextField('Тема', max_length=50, default='')
    Main_text = models.TextField('Опишите проблему')
    priority = models.CharField('Приоритет', max_length=50, choices=priority_TYPES)
    time = models.DateTimeField(auto_now_add=True),
    is_new = models.BooleanField(default=True)


    """
    def __str__(self):
        return self.title

    """
    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'