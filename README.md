# API Final YaTube

## Описание
API Final YaTube - это проект для работы с постами, комментариями, подписками и группами. Этот API предоставляет возможности для создания, редактирования и просмотра постов, комментариев, а также управления подписками и группами. Основная цель проекта - предоставить удобный интерфейс для взаимодействия с данными социальной сети.

## Установка

### Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/yourusername/api_final_yatube.git
cd api_final_yatube
```
### Cоздать и активировать виртуальное окружение:
```
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
```
### Установить зависимости из файла requirements.txt:
```pip install -r requirements.txt```

### Выполнить миграции:
```python manage.py migrate```

### Запустить проект:
```python manage.py runserver```

## Примеры запросов к API
```
Получение всех постов
GET http://127.0.0.1:8000/api/v1/posts/

Получение поста по ID
GET http://127.0.0.1:8000/api/v1/posts/{id}/

Получение комментариев к посту
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Получение комментария по ID
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

Получение всех групп
GET http://127.0.0.1:8000/api/v1/groups/

Получение группы по ID
GET http://127.0.0.1:8000/api/v1/groups/{id}/

Получение подписок
GET http://127.0.0.1:8000/api/v1/follow/

Создание JWT токена
POST http://127.0.0.1:8000/api/v1/jwt/create/
```
Пример тела запроса:
```
{
    "username": "yourusername",
    "password": "yourpassword"
}
```

## Дополнительная информация
Проект реализован с использованием Django и Django REST Framework. Описание всех доступных эндпоинтов можно найти в документации проекта.