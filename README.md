# SkyPro Модуль Django. Учебный проект: Интернет-магазин на Django + Bootstrap

[![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1+-green.svg)](https://www.djangoproject.com/)
[![Ruff](https://img.shields.io/badge/Ruff-0.16+-purple.svg)](https://docs.astral.sh/ruff/)

Учебный проект интернет-магазина на Django с Bootstrap-вёрсткой.


## 🚀 Возможности программы

Проект представляет собой интернет магазин, написанный на Python с применением фреймворка Django.
- **Главная страница** с отображением последних 5 товаров
- **Детальная страница товара** с полной информацией
- **Добавление товаров** через форму с валидацией
- **Добавление категорий** через форму
- **Страница контактов** с формой обратной связи
- **Загрузка изображений** с валидацией (размер до 0.5MB, форматы JPG/PNG/WEBP)
- **Адаптивная вёрстка** с Bootstrap 5
- **Админ-панель** для управления товарами, категориями и контактами
- **Блог** с публикацией, редактированием и удалением записей
- **Счётчик просмотров** с атомарным обновлением через `F()`
- **Пагинация в блоге** (по 8 записей)
- **Отправка email** при достижении 100 просмотров

## 📋 Содержание

- [Технологии](#технологии)
- [Установка](#установка)
- [Конфигурация](#конфигурация)
- [Использование](#использование)
- [Разработка](#разработка)
  - [Структура проекта](#структура-проекта)
  - [Линтеры и форматирование](#линтеры) 
- [Тестирование](#тестирование)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

<div id="технологии"></div>

## Технологии

| Компонент   | Технология |
|-------------|------------|
| **Язык**        | Python 3.14 |
| **Фреймворк**   | Django 6.1 |
| **База данных** | PostgreSQL |
| **ORM**         | Django ORM |
| **Вёрстка**     | Bootstrap 5 |
| **Иконки**      | Bootstrap Icons |
| **Управление зависимостями** | uv |
| **Линтинг**     | Ruff |
| **Типизация**   | MyPy |
| **Pre-commit**  | pre-commit |


<div id="установка"></div>

## Установка

```bash
git clone https://github.com/matt-motik/sp-store.git
cd sp-store
uv sync --with dev,lint
uv run python manage.py migrate
uv run python manage.py runserver
```

<div id="конфигурация"></div>

## ⚙️ Конфигурация
### Переменные окружения

Скопируй `.env.example` в `.env` и настройте:

```bash
cp .env.example .env
```
| Переменная             | Описание                  | По умолчанию        |
|------------------------|---------------------------|---------------------|
| **SECRET_KEY**         | Секретный ключ Django     | -                   |
| **DEBUG**              | Режим отладки             | True                |
| **ALLOWED_HOSTS**      | Разрешённые хосты         | localhost,127.0.0.1 |
| **DB_NAME**            | Имя базы данных PostgreSQL| -                   |
| **DB_USER**            | Пользователь PostgreSQL   | -                   |
| **DB_PASSWORD**        | Пароль PostgreSQL         | -                   |
| **DB_HOST**            | Хост PostgreSQL           | -                   |
| **DB_PORT**            | Порт PostgreSQL           | 5432                |
| **EMAIL_HOST_USER**    | Логин для email           | -                   |
| **EMAIL_HOST_PASSWORD**| Пароль приложения         | -                   |
| **DEFAULT_FROM_EMAIL** | Email отправителя         | -                   |

<div id="использование"></div>

## 💻 Использование

### Запуск программы

```bash
uv run python manage.py runserver
```
Открыть в браузере
http://127.0.0.1:8000/

### 🌐 URL-маршруты

| URL | Описание |
|-----|----------|
| `/` | Главная страница (каталог) |
| `/products/<id>/` | Детали товара |
| `/products/add/` | Добавление товара |
| `/category/add/` | Добавление категории |
| `/contacts/` | Контакты |
| `/blogs/` | Список записей блога |
| `/blogs/create/` | Создание записи |
| `/blogs/<id>/` | Детали записи |
| `/blogs/<id>/edit/` | Редактирование записи |
| `/blogs/<id>/delete/` | Удаление записи |

## 📦 Управление данными

```bash
# Очистка БД
uv run python manage.py dell_all

# Загрузка тестовых данных из фикстур
uv run python manage.py seed_db
```

## 👤 Админ-панель

```bash
# Создание суперпользователя
uv run python manage.py createsuperuser
```
Админка доступна по адресу: /admin

Зарегистрированные модели: Category, Product, Contact, BlogPost

<div id="разработка"></div>

## Разработка
<div id="структура-проекта"></div>

### Структура проекта
<!-- СЕКЦИЯ_AUTO_STRUCTURE: СТАРТ -->
<details>
<summary>📁 Структура проекта (развёрнуть)</summary>

*Этот раздел генерируется автоматически.*

```text
sp-store/
├── blog/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_blogpost_options_blogpost_updated_at.py
│   │   └── __init__.py
│   ├── templates/
│   │   └── blog/
│   │       ├── blogpost_confirm_delete.html
│   │       ├── blogpost_detail.html
│   │       ├── blogpost_form.html
│   │       └── blogpost_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── catalog/
│   ├── fixtures/
│   │   ├── categories.json
│   │   └── products.json
│   ├── management/
│   │   ├── commands/
│   │   │   ├── __init__.py
│   │   │   ├── dell_all.py
│   │   │   └── seed_db.py
│   │   └── __init__.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_contact_alter_product_name.py
│   │   └── __init__.py
│   ├── templates/
│   │   └── catalog/
│   │       ├── category_form.html
│   │       ├── contacts.html
│   │       ├── product_detail.html
│   │       ├── product_form.html
│   │       └── product_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── screenshots/
│   ├── дз1.png
│   ├── дз2.png
│   └── дз3.png
├── static/
│   ├── css/
│   │   ├── font/
│   │   │   ├── fonts/
│   │   │   │   ├── bootstrap-icons.woff
│   │   │   │   └── bootstrap-icons.woff2
│   │   │   ├── bootstrap-icons.css
│   │   │   └── bootstrap-icons.min.css
│   │   ├── bootstrap.min.css
│   │   └── bootstrap.min.css.map
│   └── js/
│       ├── bootstrap.bundle.min.js
│       ├── bootstrap.bundle.min.js.map
│       └── navigation.js
├── templates/
│   ├── include/
│   │   ├── footer.html
│   │   └── navbar.html
│   └── base.html
├── manage.py
├── pyproject.toml
├── README.md
└── uv.lock
```

</details>
<!-- СЕКЦИЯ_AUTO_STRUCTURE: КОНЕЦ -->


<div id="линтеры"></div>

### 🔍 Линтеры и форматирование

Проект использует `ruff` для линтинга и форматирования, `mypy` для проверки типов.

### Проверка кода

```bash
# Линтинг
uv run ruff check catalog/ blog/ config/

# Автоисправление ошибок
uv run ruff check --fix catalog/ blog/ config/

# Форматирование
uv run ruff format catalog/ blog/ config/

# Проверка типов
uv run mypy catalog/ blog/ config/
```
### Pre-commit hooks
```bash
# Установить hooks (выполняется автоматически перед каждым коммитом)
uv run pre-commit install

# Проверить все файлы вручную
uv run pre-commit run --all-files
```

<!-- СЕКЦИЯ_AUTO_API: СТАРТ -->
<details>
<summary>📚 Документация API (развёрнуть)</summary>

*Этот раздел генерируется автоматически из docstring.*

| Модуль | Функция/Класс | Краткое описание |
|--------|---------------|------------------|
| [**`admin.py`**](docs/api/admin.md) | | |
| | [📦 CategoryAdmin](docs/api/admin.md#CategoryAdmin) | Настройки административной панели Категорий. |
| | [📦 ProductAdmin](docs/api/admin.md#ProductAdmin) | Настройки административной панели Продуктов. |
| | [📦 ContactAdmin](docs/api/admin.md#ContactAdmin) | Настройки административной панели Контактов. |
| | [📦 BlogPostAdmin](docs/api/admin.md#BlogPostAdmin) | Настройки административной панели записи блога. |
| [**`apps.py`**](docs/api/apps.md) | | |
| | [📦 CatalogConfig](docs/api/apps.md#CatalogConfig) | Конфигурация приложения каталога. |
| | [📦 BlogConfig](docs/api/apps.md#BlogConfig) | Конфигурация приложения блога. |
| [**`dell_all.py`**](docs/api/dell_all.md) | | |
| | [📦 Command](docs/api/dell_all.md#Command) | Команда удаления. |
| | [⚙️ Command.handle](docs/api/dell_all.md#Command.handle) | Хенндл. |
| | [🔧 handle](docs/api/dell_all.md#handle) | Хенндл. |
| [**`forms.py`**](docs/api/forms.md) | | |
| | [📦 CategoryForm](docs/api/forms.md#CategoryForm) | Форма для создания и редактирования категории. |
| | [📦 ProductForm](docs/api/forms.md#ProductForm) | Форма для создания и редактирования товара. |
| | [⚙️ ProductForm.clean_price](docs/api/forms.md#ProductForm.clean_price) | Проверяет, что цена больше 0. |
| | [⚙️ ProductForm.clean_image](docs/api/forms.md#ProductForm.clean_image) | Проверяет, что размер изображение не больше 0.5MB. И тип JPG, PNG, WEBP. |
| | [📦 Meta](docs/api/forms.md#Meta) | Внутренний класс с настройками формы. |
| | [📦 Meta](docs/api/forms.md#Meta) | Внутренний класс с настройками формы. |
| | [🔧 clean_price](docs/api/forms.md#clean_price) | Проверяет, что цена больше 0. |
| | [🔧 clean_image](docs/api/forms.md#clean_image) | Проверяет, что размер изображение не больше 0.5MB. И тип JPG, PNG, WEBP. |
| | [📦 BlogPostForm](docs/api/forms.md#BlogPostForm) | Форма для создания и редактирования записи блога. |
| | [⚙️ BlogPostForm.clean_preview](docs/api/forms.md#BlogPostForm.clean_preview) | Проверяет, что размер изображение не больше 0.5MB. И тип JPG, PNG, WEBP. |
| | [📦 Meta](docs/api/forms.md#Meta) | Внутренний класс с настройками формы. |
| | [🔧 clean_preview](docs/api/forms.md#clean_preview) | Проверяет, что размер изображение не больше 0.5MB. И тип JPG, PNG, WEBP. |
| [**`manage.py`**](docs/api/manage.md) | | |
| | [🔧 main](docs/api/manage.md#main) | Run administrative tasks. |
| [**`models.py`**](docs/api/models.md) | | |
| | [📦 Category](docs/api/models.md#Category) | Модель категории товаров. |
| | [📦 Product](docs/api/models.md#Product) | Модель товара. |
| | [📦 Contact](docs/api/models.md#Contact) | Модель контактных данных компании. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета для админки. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета для админки. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета для админки. |
| | [📦 BlogPost](docs/api/models.md#BlogPost) | Модель записи в блоге. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета-параметры модели BlogPost. |
| [**`seed_db.py`**](docs/api/seed_db.md) | | |
| | [📦 Command](docs/api/seed_db.md#Command) | Команда засеивания базы тестовыми данными. |
| | [⚙️ Command.handle](docs/api/seed_db.md#Command.handle) | Хенндл. |
| | [🔧 handle](docs/api/seed_db.md#handle) | Хенндл. |
| [**`views.py`**](docs/api/views.md) | | |
| | [📦 ProductListView](docs/api/views.md#ProductListView) | Представление для отображения списка товаров с пагинацией. |
| | [⚙️ ProductListView.get_queryset](docs/api/views.md#ProductListView.get_queryset) | Возвращает отсортированный список товаров. |
| | [📦 ProductDetailView](docs/api/views.md#ProductDetailView) | Представление для отображения товара. |
| | [📦 ContactsView](docs/api/views.md#ContactsView) | Отображает страницу контактов и обрабатывает форму обратной связи. |
| | [⚙️ ContactsView.get](docs/api/views.md#ContactsView.get) | Получение данных о контакте для связи. |
| | [⚙️ ContactsView.post](docs/api/views.md#ContactsView.post) | Отправка обратной связи. |
| | [📦 ProductCreateView](docs/api/views.md#ProductCreateView) | Представление для добавления товара. |
| | [⚙️ ProductCreateView.get_success_url](docs/api/views.md#ProductCreateView.get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [⚙️ ProductCreateView.form_valid](docs/api/views.md#ProductCreateView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 CategoryCreateView](docs/api/views.md#CategoryCreateView) | Представление для добавления категории. |
| | [⚙️ CategoryCreateView.get_success_url](docs/api/views.md#CategoryCreateView.get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [⚙️ CategoryCreateView.form_valid](docs/api/views.md#CategoryCreateView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 get_queryset](docs/api/views.md#get_queryset) | Возвращает отсортированный список товаров. |
| | [🔧 get](docs/api/views.md#get) | Получение данных о контакте для связи. |
| | [🔧 post](docs/api/views.md#post) | Отправка обратной связи. |
| | [🔧 get_success_url](docs/api/views.md#get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 get_success_url](docs/api/views.md#get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 BlogPostDetailView](docs/api/views.md#BlogPostDetailView) | Представление для отображения записи. |
| | [⚙️ BlogPostDetailView.get_object](docs/api/views.md#BlogPostDetailView.get_object) | Переопредение данных записи, для увеличения счётчика просмотров. |
| | [⚙️ BlogPostDetailView.send_congratulation_email](docs/api/views.md#BlogPostDetailView.send_congratulation_email) | Отправляет поздравление о достижении 100 просмотров. |
| | [📦 BlogPostListView](docs/api/views.md#BlogPostListView) | Представление для отображения списка опубликованных записей в блоге. |
| | [⚙️ BlogPostListView.get_queryset](docs/api/views.md#BlogPostListView.get_queryset) | Возвращает отсортированный список записей. |
| | [📦 BlogPostCreateView](docs/api/views.md#BlogPostCreateView) | Представление для добавления записи блога. |
| | [⚙️ BlogPostCreateView.get_success_url](docs/api/views.md#BlogPostCreateView.get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [📦 BlogPostUpdateView](docs/api/views.md#BlogPostUpdateView) | Представление для редактирования записи блога. |
| | [⚙️ BlogPostUpdateView.get_success_url](docs/api/views.md#BlogPostUpdateView.get_success_url) | Возвращает URL для перенаправления после успешного редактирования. |
| | [⚙️ BlogPostUpdateView.form_valid](docs/api/views.md#BlogPostUpdateView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 BlogPostDeleteView](docs/api/views.md#BlogPostDeleteView) | Представление для удаления записи блога. |
| | [⚙️ BlogPostDeleteView.form_valid](docs/api/views.md#BlogPostDeleteView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 get_object](docs/api/views.md#get_object) | Переопредение данных записи, для увеличения счётчика просмотров. |
| | [🔧 send_congratulation_email](docs/api/views.md#send_congratulation_email) | Отправляет поздравление о достижении 100 просмотров. |
| | [🔧 get_queryset](docs/api/views.md#get_queryset) | Возвращает отсортированный список записей. |
| | [🔧 get_success_url](docs/api/views.md#get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [🔧 get_success_url](docs/api/views.md#get_success_url) | Возвращает URL для перенаправления после успешного редактирования. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |

> 📘 **Полная документация** с примерами и описанием параметров доступна в папке [`docs/api`](docs/api).
</details>
<!-- СЕКЦИЯ_AUTO_API: КОНЕЦ -->

<div id="тестирование"></div>

## 🧪 Тестирование
Тесты находятся в папке `tests/` (если есть) или будут добавлены позже.
<!-- СЕКЦИЯ_AUTO_TEST: СТАРТ -->
<details>
<summary>📊 Результаты тестов и покрытие (развёрнуть)</summary>
### 📊 Результаты тестов SRC

```
🎯 Результаты тестов src:
============================= test session starts ==============================
=============================== warnings summary ===============================
============================== 1 warning in 0.02s ==============================
```

> 📊 **HTML отчёт покрытия**: [`htmlcov/index.html`](htmlcov/src/index.html)


</details>
<!-- СЕКЦИЯ_AUTO_TEST: КОНЕЦ -->

<div id="to-do"></div>

## To do

- [x] Структура проекта, `pyproject.toml`, `README.md`, `.gitignore`, uv, линтеры
- [x] Виртуальное окружение, установка зависимостей через uv
- [x] `readme_gen.py` — скрипт генерации README и покрытия тестами
- [x] Инициализация Django-проекта
- [x] Приложение catalog с URL-роутингом
- [x] Шаблоны home и contacts с Bootstrap
- [x] Форма обратной связи с POST-обработкой
- [x] Подключение PostgreSQL, настройка `.env`
- [x] Модели `Category`, `Product`, `Contact`
- [x] Миграции и регистрация в админке
- [x] Кастомные команды `dell_all` и `seed_db`
- [x] Фикстуры для `Category` и `Product`
- [x] Отображение контактов из БД на странице контактов
- [x] Детальная страница товара (`/products/<id>/`)
- [x] Добавление товаров через форму (`/products/add/`)
- [x] Добавление категорий через форму (`/category/add/`)
- [x] Валидация изображений (размер 0.5MB, форматы JPG/PNG/WEBP)
- [x] Пагинация на главной странице (по 8 товаров)
- [x] Скриншоты shell-команд в `screenshots/`
- [x] Приложение blog с URL-роутингом
- [x] Модель BlogPost с миграциями
- [x] Форма BlogPostForm с валидацией
- [x] Шаблоны блога (list, detail, form, confirm_delete)
- [x] Пагинация в блоге (по 8 записей)
- [x] Счётчик просмотров с атомарным обновлением
- [x] Отправка email при 100 просмотрах
- [x] Настройка админки для BlogPost
- [x] Проверить линтеры (`ruff`, `mypy`)
- [x] Финальная вычитка документации и обновление README
- [x] Обновить документацию

## Команда проекта

- Matvey Bakirov — [mabakirov@gmail.com](mailto:mabakirov@gmail.com) — Back-End Engineer
