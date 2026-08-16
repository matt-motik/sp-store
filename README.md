# SkyPro Модуль Django. Учебный проект: Интернет-магазин на Django + Bootstrap

[![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1+-green.svg)](https://www.djangoproject.com/)
[![Ruff](https://img.shields.io/badge/Ruff-0.16+-purple.svg)](https://docs.astral.sh/ruff/)

Учебный проект интернет-магазина на Django с Bootstrap-вёрсткой.


## 🚀 Возможности программы

Проект представляет собой интернет магазин, написанный на Python с применением фреймворка Django.


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
| **Django**  | `https://www.djangoproject.com/` |
| **Верстка** | Bootstrap 5 |
| **Иконки**  | Bootstrap Icons |


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
| Переменная   | Описание | По умолчанию        |
|-------------|------------|---------------------|
| **SECRET_KEY**  | Секретный ключ Django | - |
| **DEBUG** | Режим отладки| True | 
| **ALLOWED_HOSTS**  | Разрешённые хосты | localhost,127.0.0.1 |

<div id="использование"></div>

## 💻 Использование

### Запуск программы

```bash
uv run python manage.py runserver
```
Открыть в браузере
http://127.0.0.1:8000/

<div id="разработка"></div>

## Разработка
<div id="структура-проекта"></div>

### Структура проекта
```
sp-store/
├── config/              # конфигурация Django
├── catalog/             # приложение каталога
│   ├── templates/       # шаблоны home.html, contacts.html
│   └── views.py         # контроллеры
├── static/              # Bootstrap, иконки, JS
├── templates/           # глобальные шаблоны (если есть)
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
| [**`apps.py`**](docs/api/apps.md) | | |
| | [📦 CatalogConfig](docs/api/apps.md#CatalogConfig) | Конфигурация приложения каталога. |
| [**`manage.py`**](docs/api/manage.md) | | |
| | [🔧 main](docs/api/manage.md#main) | Run administrative tasks. |
| [**`views.py`**](docs/api/views.md) | | |
| | [🔧 home](docs/api/views.md#home) | Отображает главную страницу магазина. |
| | [🔧 contacts](docs/api/views.md#contacts) | Отображает страницу контактов и обрабатывает форму обратной связи. |

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
- [x] Проверить линтеры (`ruff`, `mypy`)
- [x] Финальная вычитка документации и обновление README
- [x] Обновить документацию

## Команда проекта

- Matvey Bakirov — [mabakirov@gmail.com](mailto:mabakirov@gmail.com) — Back-End Engineer
