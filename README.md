# pulsar-test
Тестовое задание для компании ПУЛЬСАР-МСК.

## Описание

### Модели

Создать модель товара со следущими полями:
- Название
- Артикул
- Цена
- Статус
- Изображение

Статус должен принимать одно из нескольких значений:
- В наличии
- Нет в наличии
- Ожидается
- Не производится
- Под заказ

### Дополнительные требования к сериализаторам

Сериализатор товара должен возвращать данные изображения в виде
- относительный адрес к файлу изображения без расширения 
- список доступных расширений для данного изображения

При этом требуется реализовать механизм конвертации изображения при загрузке из форматов PNG или JPG в формат WEBP.
Строго JPG/PNG -> WEBP. Вывод всех доступных расширений.

## Установка и запуск
- Склонируйте репозиторий на свой компьютер
- Создайте виртуальное окружение и активируйте его
- Установите зависимости из файла requirements.txt
- Выполните миграции командой `python manage.py migrate`
- Запустите сервер командой `python manage.py runserver`
- Сервер будет доступен по адресу http://127.0.0.1:8000/

## Примеры запросов

- Получение списка товаров
```
GET http://127.0.0.1:8000/api/products/
[
    {
        "id": 1,
        "name": "Cup",
        "code": "1234UF",
        "price": "10.00",
        "status": "in stock",
        "image": "http://127.0.0.1:8000/media/images/cup.jpg"
    },
    {
        "id": 2,
        "name": "Plate",
        "code": "1234US",
        "price": "12.00",
        "status": "in stock",
        "image": "http://127.0.0.1:8000/media/images/plate.jpg"
    }
]
```

- Получение товара по id
```
GET http://127.0.0.1:8000/api/products/1/
{
    "id": 11,
    "image": {
        "path": "/media/images/wave",
        "formats": [
            "webp",
            "jpg"
        ]
    },
    "name": "Image",
    "code": "1234",
    "price": "10.00",
    "status": "in stock"
}
```

- Создание товара
```
POST http://127.0.0.1:8000/api/products/
```