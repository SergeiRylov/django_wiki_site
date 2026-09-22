# django-wiki-site

**django-wiki-site** — полнофункциональный сайт, реализующий простейшую Wiki на Django.

## Возможности

- Создание и редактирование статей
- Хранение истории изменений
- Локализация интерфейса (русский язык)
- Модульная архитектура: `app_base`, `app_wiki`

## Установка

### 1. Клонирование

```bash
git clone https://github.com/SergeiRylov/django_wiki_site.git
cd django_wiki_site
```

### 2. Виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv/bin/activate         # Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Миграции и запуск

```bash
python manage.py migrate
python manage.py runserver
```

Сайт будет доступен по адресу: http://127.0.0.1:8000/

## Зависимости

Проект использует собственные Django-приложения:

- `app_base` — базовые утилиты и модели
- `app_wiki` — логика Wiki

Полный список — в [requirements.txt](requirements.txt).

## Локализация

Проект поддерживает русский язык. Файлы переводов находятся в `locale/ru/LC_MESSAGES/`.

Для компиляции переводов:

```bash
python manage.py compilemessages
```

## Лицензия

См. файл [LICENSE](LICENSE).

## Автор

**Sergei Rylov** — [@SergeiRylov](https://github.com/SergeiRylov)