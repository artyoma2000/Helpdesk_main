# Форма технической поддержки для "АО Фазатрон-НИИР"

## Описание проекта: 
Изначально, была поставлена задача собрать простую форму для заявок для корпоративной системы Helpdesk. Так как Рабочий комп есть в каждом кабинете, а техподдержка постоянно перемещается, пытаясь решить проблемы пользователей, было решено прикрутить для оповещения асинхронного Телеграмм бота, который способен в режиме реального времени оповестить исполнителя о том, что ему поступила ещё одна заявка. 

Ситема проста как мир: Заявка - добавление заявки в базу - отметка о получении, которую оставляет бот, когда пересылает текст заявки исполнителю.  

## Список технологий: 
- Django
- PostgresSQL
- TelegramAPI
- asyncio
- pydantic
- psycopg2
- aiogram
- JSON

## Фронт: 
![image](https://github.com/artyoma2000/Helpdesk_main/assets/70951593/b4590c26-ea86-4869-9b06-70ed112306eb)

## Ответ бота: 
![image](https://github.com/artyoma2000/Helpdesk_main/assets/70951593/0c42c1c7-5bae-4e7a-a8a5-fbcce12e2d30)

## Возможное дальнейшее развитие:
- Было бы славно, если бы получилось нарастить список исполнителей (Пока работает только с рабочим аккаунтом).
- Переработать информацию, которую выдает телеграмм-бот (Пока что работает в тестовом режиме и выдает только некоторые параметры).
- Доработать Саму форму, возможно, добавить новые фитчи.
- Возможно, разнести на микросервисную архитектуру (Забавы ради).
- Необходимо доработать таблицу исполнителей с учетом их статуса (В отпуке и.т.д)
- Возможно, добавлю админскую панель для Телеграмм бота, чтобы можно было редактировать прямо через него. 
