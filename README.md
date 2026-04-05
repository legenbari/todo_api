# 📝 FastAPI Notes API

Простой CRUD API для заметок, написанный с использованием **FastAPI** и **SQLAlchemy (async)**.

## 🚀 Возможности

* Создание заметки
* Получение всех заметок
* Получение заметки по ID
* Обновление заметки
* Удаление заметки

## 🛠️ Стек технологий

* FastAPI
* SQLAlchemy (async)
* PostgreSQL
* Pydantic

## 📁 Структура проекта

```
.
├── main.py        # Точки входа (роуты)
├── models.py      # Модели и подключение к БД
├── crud.py        # CRUD-операции
├── schemas.py     # Pydantic схемы
├── config.py      # Конфигурация БД
```

## ⚙️ Настройка

1. Установите зависимости:

```bash
pip install fastapi uvicorn sqlalchemy asyncpg
```

2. Заполните `config.py`:

```python
PASSWORD = "your_password"
LOGIN = "your_login"
HOST = "localhost"
PORT = "5432"
DB_NAME = "your_db"
```

3. Создайте таблицы (например через Alembic или вручную).

## ▶️ Запуск

```bash
uvicorn main:app --reload
```

Документация будет доступна по адресу:

```
http://127.0.0.1:8000/docs
```

## 📌 Эндпоинты

### ➕ Создать заметку

`POST /note/post`

### 📖 Получить все заметки

`GET /note/get`

### 🔍 Получить заметку по ID

`GET /note/get/{note_id}`

### ✏️ Обновить заметку

`PUT /note/put/{note_id}`

### ❌ Удалить заметку

`DELETE /note/delete/{note_id}`

## 📄 Пример запроса

```json
{
  "title": "Моя заметка",
  "content": "Текст заметки"
}
```

## ⚠️ Примечания

* Все операции выполняются асинхронно
* При отсутствии записи возвращается ошибка 404
* Поля `title` и `content` имеют ограничения по длине

---

💡 Проект подходит как стартовый шаблон для CRUD API на FastAPI.
