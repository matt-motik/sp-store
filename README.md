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
| Переменная       | Описание                    | По умолчанию        |
|------------------|-----------------------------|---------------------|
| **SECRET_KEY**   | Секретный ключ Django       | -                   |
| **DEBUG**        | Режим отладки               | True                |
| **ALLOWED_HOSTS**| Разрешённые хосты           | localhost,127.0.0.1 |
| **DB_NAME**      | Имя базы данных PostgreSQL  | -                   |
| **DB_USER**      | Пользователь PostgreSQL     | -                   |
| **DB_PASSWORD**  | Пароль PostgreSQL           | -                   |
| **DB_HOST**      | Хост PostgreSQL             | -                   |
| **DB_PORT**      | Порт PostgreSQL             | 5432                |

<div id="использование"></div>

## 💻 Использование

### Запуск программы

```bash
uv run python manage.py runserver
```
Открыть в браузере
http://127.0.0.1:8000/


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

Зарегистрированные модели: Category, Product, Contact

<div id="разработка"></div>

## Разработка
<div id="структура-проекта"></div>

### Структура проекта
```
sp-store/
├── config/              # конфигурация Django
├── catalog/             # приложение каталога
│   ├── templates/       # шаблоны home.html, contacts.html
│   │   ├── include/             # Включаемые шаблоны
│   │   │   ├── navbar.html      # Навигация
│   │   │   └── footer.html      # Подвал
│   │   ├── base.html            # Базовый шаблон
│   │   ├── home.html            # Главная страница
│   │   ├── product_detail.html  # Детали товара
│   │   ├── add_product.html     # Добавление товара
│   │   ├── add_category.html    # Добавление категории
│   │   └── contacts.html        # Страница контактов
│   ├── admin.py             # Настройки админки
│   ├── forms.py             # Формы (ProductForm, CategoryForm)
│   ├── models.py            # Модели (Category, Product, Contact)
│   └── views.py         # контроллеры
├── static/              # Bootstrap, иконки, JS
├── media/                   # Загруженные пользователем файлы
├── docs/                    # Документация
├── screenshots/             # Скриншоты
├── manage.py
├── pyproject.toml       # uv + ruff + mypy
└── README.md
```
<div id="линтеры"></div>

### 🔍 Линтеры и форматирование

Проект использует `ruff` для линтинга и форматирования, `mypy` для проверки типов.

### Проверка кода

```bash
# Линтинг
uv run ruff check catalog/ config/

# Автоисправление ошибок
uv run ruff check --fix catalog/ config/

# Форматирование
uv run ruff format catalog/ config/

# Проверка типов
uv run mypy catalog/ config/
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
| [**`apps.py`**](docs/api/apps.md) | | |
| | [📦 CatalogConfig](docs/api/apps.md#CatalogConfig) | Конфигурация приложения каталога. |
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
| [**`manage.py`**](docs/api/manage.md) | | |
| | [🔧 main](docs/api/manage.md#main) | Run administrative tasks. |
| [**`models.py`**](docs/api/models.md) | | |
| | [📦 Category](docs/api/models.md#Category) | Модель категории товаров. |
| | [📦 Product](docs/api/models.md#Product) | Модель товара. |
| | [📦 Contact](docs/api/models.md#Contact) | Модель контактных данных компании. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета для админки. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета для админки. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета для админки. |
| [**`seed_db.py`**](docs/api/seed_db.md) | | |
| | [📦 Command](docs/api/seed_db.md#Command) | Команда засеивания базы тестовыми данными. |
| | [⚙️ Command.handle](docs/api/seed_db.md#Command.handle) | Хенндл. |
| | [🔧 handle](docs/api/seed_db.md#handle) | Хенндл. |
| [**`views.py`**](docs/api/views.md) | | |
| | [🔧 home](docs/api/views.md#home) | Отображает главную страницу магазина с пагинацией. |
| | [🔧 product_detail](docs/api/views.md#product_detail) | Отображает подробную информацию о продукте. |
| | [🔧 contacts](docs/api/views.md#contacts) | Отображает страницу контактов и обрабатывает форму обратной связи. |
| | [🔧 add_product](docs/api/views.md#add_product) | Отображает страницу добавления товара и обрабатывает форму добавления. |
| | [🔧 add_category](docs/api/views.md#add_category) | Отображает страницу добавления категории и обрабатывает форму добавления. |

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
============================== 1 warning in 0.01s ==============================
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
- [x] Вывод последних 5 продуктов на главной
- [x] Отображение контактов из БД на странице контактов
- [x] Детальная страница товара (`/products/<id>/`)
- [x] Добавление товаров через форму (`/products/add/`)
- [x] Добавление категорий через форму (`/category/add/`)
- [x] Валидация изображений (размер 0.5MB, форматы JPG/PNG/WEBP)
- [x] Пагинация на главной странице (по 8 товаров)
- [x] Скриншоты shell-команд в `screenshots/`
- [x] Проверить линтеры (`ruff`, `mypy`)
- [x] Финальная вычитка документации и обновление README
- [x] Обновить документацию

## Команда проекта

- Matvey Bakirov — [mabakirov@gmail.com](mailto:mabakirov@gmail.com) — Back-End Engineer
