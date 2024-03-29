# Generated by Django 4.2.9 on 2024-01-31 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recipient', models.TextField(default='', max_length=50, verbose_name='ФИО получателя')),
                ('Service', models.CharField(choices=[('ИТ Отдел', 'ИТ Отдел')], max_length=50, verbose_name='Сервис')),
                ('Location', models.CharField(choices=[('Авиационный переулок', 'Авиационный переулок'), ('Кавказский бульвар', 'Кавказский бульвар'), ('Электрический переулок', 'Электрический переулок')], max_length=250, verbose_name='Расположение')),
                ('Office', models.TextField(default='', max_length=50, verbose_name='Кабинет')),
                ('Floor', models.TextField(default='', max_length=50, verbose_name='Этаж')),
                ('Building', models.TextField(default='', max_length=50, verbose_name='Корпус')),
                ('Topic', models.TextField(default='', max_length=50, verbose_name='Тема')),
                ('Main_text', models.TextField(verbose_name='Опишите проблему')),
                ('priority', models.CharField(choices=[('Низкий', 'Низкий'), ('Нормальный', 'Нормальный'), ('Высокий', 'Высокий')], max_length=50, verbose_name='Приоритет')),
                ('is_new', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
