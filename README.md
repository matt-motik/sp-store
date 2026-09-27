# SkyPro Модуль Django. Учебный проект: Интернет-магазин на Django + Bootstrap

[![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1+-green.svg)](https://www.djangoproject.com/)
[![Ruff](https://img.shields.io/badge/Ruff-0.16+-purple.svg)](https://docs.astral.sh/ruff/)

Учебный проект интернет-магазина на Django с Bootstrap-вёрсткой.


## 🚀 Возможности программы

Проект представляет собой интернет магазин, написанный на Python с применением фреймворка Django.
- **Главная страница** с отображением последних 8 товаров
- **Детальная страница товара** с полной информацией
- **Добавление товаров** через форму с валидацией
- **Редактирование товаров** через форму с валидацией
- **Удаление товаров** с подтверждением
- **Добавление категорий** через форму
- **Редактирование категорий** через форму
- **Удаление категорий** с подтверждением
- **Список категорий** с количеством товаров в каждой
- **Фильтрация товаров по категории**
- **Страница контактов** с формой обратной связи
- **Загрузка изображений** с валидацией (размер до 0.5MB, форматы JPG/PNG/WEBP)
- **Адаптивная вёрстка** с Bootstrap 5
- **Админ-панель** для управления товарами, категориями, контактами и пользователями
- **Блог** с публикацией, редактированием и удалением записей
- **Счётчик просмотров** с атомарным обновлением через `F()`
- **Пагинация в блоге** (по 8 записей)
- **Отправка email** при достижении 100 просмотров
- **Регистрация пользователей** с подтверждением пароля
- **Активация аккаунта** по email через токен
- **Авторизация** по email и паролю
- **Выход из системы** через POST-форму
- **Просмотр и редактирование профиля** пользователя
- **Смена пароля** пользователя
- **Защита CRUD операций** от анонимных пользователей
- **Владелец товара** с ограничением доступа к неопубликованным товарам
- **Снятие товара с публикации** отдельной кнопкой для модераторов
- **Владелец записи блога** с автоподстановкой при создании
- **Страница «Мои записи»** в блоге
- **Черновики записей** видны только роли с правом изменения
- **Роли и группы прав**: «Модератор продуктов», «Контент-менеджер»
- **Разграничение прав** на страницах и в админ-панели

## 📋 Содержание

- [Технологии](#технологии)
- [Установка](#установка)
- [Конфигурация](#конфигурация)
- [Использование](#использование)
- [Роли и права](#роли-и-права)
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
| `/products/<id>/edit/` | Редактирование товара |
| `/products/<id>/delete/` | Удаление товара |
| `/categories/` | Список категорий |
| `/category/add/` | Добавление категории |
| `/category/<id>/edit/` | Редактирование категории |
| `/category/<id>/delete/` | Удаление категории |
| `/contacts/` | Контакты |
| `/blogs/` | Список записей блога |
| `/blogs/mine/` | Мои записи |
| `/blogs/create/` | Создание записи |
| `/blogs/<id>/` | Детали записи |
| `/blogs/<id>/edit/` | Редактирование записи |
| `/blogs/<id>/delete/` | Удаление записи |
| `/users/register/` | Регистрация |
| `/users/login/` | Вход |
| `/users/logout/` | Выход |
| `/users/activate/<uidb64>/<token>/` | Активация аккаунта по email |
| `/users/profile/` | Просмотр профиля |
| `/users/profile/edit/` | Редактирование профиля |
| `/users/password/change/` | Смена пароля |

## 📦 Управление данными

```bash
# Очистка БД
uv run python manage.py dell_all

# Загрузка тестовых данных из фикстур
uv run python manage.py seed_db

# Создание групп и выдача ролей
uv run python manage.py create_moderator_group
uv run python manage.py add_moderator --email=moderator@example.com --password=secret123
uv run python manage.py create_content_manager_group
uv run python manage.py add_content_manager --email=content@example.com --password=secret123
```

## 👤 Админ-панель

```bash
# Создание суперпользователя
uv run python manage.py createsuperuser
```
Админка доступна по адресу: /admin

Зарегистрированные модели: Category, Product, Contact, BlogPost, CustomUser

<div id="роли-и-права"></div>

## 👥 Роли и права

Права выдаются через группы. Пользователь с ролью получает `is_staff` и работает в админ-панели в пределах прав своей группы.

| Группа | Права в админ-панели |
|--------|----------------------|
| **Модератор продуктов** | Товары и категории: просмотр, создание, редактирование, удаление, снятие товара с публикации |
| **Контент-менеджер** | Записи блога: просмотр, создание, редактирование, удаление |
| **Суперпользователь** | Полный доступ ко всем разделам |

Права на страницах сайта:

- товар создаёт любой авторизованный пользователь, редактирует владелец, удаляет владелец или модератор продуктов;
- снять товар с публикации может модератор продуктов;
- категории создаёт, редактирует и удаляет модератор продуктов;
- записи блога создаёт, редактирует и удаляет контент-менеджер, черновики видны только контент-менеджеру и суперпользователю.

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
│   ├── fixtures/
│   │   └── blogposts.json
│   ├── management/
│   │   ├── commands/
│   │   │   ├── __init__.py
│   │   │   ├── add_content_manager.py
│   │   │   └── create_content_manager_group.py
│   │   └── __init__.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_blogpost_options_blogpost_updated_at.py
│   │   ├── 0003_blogpost_owner.py
│   │   └── __init__.py
│   ├── templates/
│   │   └── blog/
│   │       ├── blogpost_confirm_delete.html
│   │       ├── blogpost_detail.html
│   │       ├── blogpost_form.html
│   │       ├── blogpost_list.html
│   │       └── blogpost_mine.html
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
│   │   ├── contacts.json
│   │   ├── products.json
│   │   └── users.json
│   ├── management/
│   │   ├── commands/
│   │   │   ├── __init__.py
│   │   │   ├── add_moderator.py
│   │   │   ├── create_moderator_group.py
│   │   │   ├── dell_all.py
│   │   │   └── seed_db.py
│   │   └── __init__.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_contact_alter_product_name.py
│   │   ├── 0003_product_in_stock.py
│   │   ├── 0004_alter_product_options_product_is_published.py
│   │   ├── 0005_product_owner.py
│   │   └── __init__.py
│   ├── templates/
│   │   └── catalog/
│   │       ├── category_confirm_delete.html
│   │       ├── category_form.html
│   │       ├── category_list.html
│   │       ├── contacts.html
│   │       ├── product_confirm_delete.html
│   │       ├── product_detail.html
│   │       ├── product_form.html
│   │       ├── product_list.html
│   │       └── product_unpublish.html
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
│   ├── mixins.py
│   ├── settings.py
│   ├── urls.py
│   ├── validators.py
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
├── users/
│   ├── management/
│   │   ├── commands/
│   │   │   ├── __init__.py
│   │   │   └── addsu.py
│   │   └── __init__.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_customuser_managers.py
│   │   └── __init__.py
│   ├── templates/
│   │   └── users/
│   │       ├── activation_invalid.html
│   │       ├── activation_sent.html
│   │       ├── logged_out.html
│   │       ├── login.html
│   │       ├── password_change.html
│   │       ├── profile.html
│   │       ├── profile_form.html
│   │       └── register.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── managers.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
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
uv run ruff check catalog/ blog/ config/ users/

# Автоисправление ошибок
uv run ruff check --fix catalog/ blog/ config/ users/

# Форматирование
uv run ruff format catalog/ blog/ config/ users/

# Проверка типов
uv run mypy catalog/ blog/ config/ users/
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
| [**`add_content_manager.py`**](docs/api/add_content_manager.md) | | |
| | [📦 Command](docs/api/add_content_manager.md#Command) | Добавляет пользователя в группу «Контент-менеджер». |
| | [⚙️ Command.add_arguments](docs/api/add_content_manager.md#Command.add_arguments) | Добавляет аргументы командной строки. |
| | [⚙️ Command.handle](docs/api/add_content_manager.md#Command.handle) | Создаёт или обновляет пользователя и добавляет его в группу. |
| | [🔧 add_arguments](docs/api/add_content_manager.md#add_arguments) | Добавляет аргументы командной строки. |
| | [🔧 handle](docs/api/add_content_manager.md#handle) | Создаёт или обновляет пользователя и добавляет его в группу. |
| [**`add_moderator.py`**](docs/api/add_moderator.md) | | |
| | [📦 Command](docs/api/add_moderator.md#Command) | Добавляет пользователя в группу «Модератор продуктов». |
| | [⚙️ Command.add_arguments](docs/api/add_moderator.md#Command.add_arguments) | Добавляет аргументы командной строки. |
| | [⚙️ Command.handle](docs/api/add_moderator.md#Command.handle) | Создаёт или обновляет пользователя и добавляет его в группу. |
| | [🔧 add_arguments](docs/api/add_moderator.md#add_arguments) | Добавляет аргументы командной строки. |
| | [🔧 handle](docs/api/add_moderator.md#handle) | Создаёт или обновляет пользователя и добавляет его в группу. |
| [**`addsu.py`**](docs/api/addsu.md) | | |
| | [📦 Command](docs/api/addsu.md#Command) | Создаёт суперпользователя с указанными email и паролем. |
| | [⚙️ Command.add_arguments](docs/api/addsu.md#Command.add_arguments) | Добавляет аргументы командной строки. |
| | [⚙️ Command.handle](docs/api/addsu.md#Command.handle) | Создаёт или обновляет суперпользователя. |
| | [🔧 add_arguments](docs/api/addsu.md#add_arguments) | Добавляет аргументы командной строки. |
| | [🔧 handle](docs/api/addsu.md#handle) | Создаёт или обновляет суперпользователя. |
| [**`admin.py`**](docs/api/admin.md) | | |
| | [📦 CategoryAdmin](docs/api/admin.md#CategoryAdmin) | Настройки административной панели Категорий. |
| | [📦 ProductAdmin](docs/api/admin.md#ProductAdmin) | Настройки административной панели Продуктов. |
| | [📦 ContactAdmin](docs/api/admin.md#ContactAdmin) | Настройки административной панели Контактов. |
| | [📦 BlogPostAdmin](docs/api/admin.md#BlogPostAdmin) | Настройки административной панели записи блога. |
| | [📦 CustomUserAdmin](docs/api/admin.md#CustomUserAdmin) | Настройки административной панели для модели CustomUser. |
| | [⚙️ CustomUserAdmin.get_fieldsets](docs/api/admin.md#CustomUserAdmin.get_fieldsets) | Возвращает fieldsets в зависимости от режима (создание/редактирование). |
| | [🔧 get_fieldsets](docs/api/admin.md#get_fieldsets) | Возвращает fieldsets в зависимости от режима (создание/редактирование). |
| [**`apps.py`**](docs/api/apps.md) | | |
| | [📦 CatalogConfig](docs/api/apps.md#CatalogConfig) | Конфигурация приложения каталога. |
| | [📦 BlogConfig](docs/api/apps.md#BlogConfig) | Конфигурация приложения блога. |
| | [📦 UsersConfig](docs/api/apps.md#UsersConfig) | Конфигурация приложения users. |
| [**`create_content_manager_group.py`**](docs/api/create_content_manager_group.md) | | |
| | [📦 Command](docs/api/create_content_manager_group.md#Command) | Создаёт группу «Контент-менеджер» и назначает ей права на записи блога. |
| | [⚙️ Command.add_arguments](docs/api/create_content_manager_group.md#Command.add_arguments) | Добавляет аргументы командной строки. |
| | [⚙️ Command.handle](docs/api/create_content_manager_group.md#Command.handle) | Создаёт группу и назначает ей права на записи блога. |
| | [🔧 add_arguments](docs/api/create_content_manager_group.md#add_arguments) | Добавляет аргументы командной строки. |
| | [🔧 handle](docs/api/create_content_manager_group.md#handle) | Создаёт группу и назначает ей права на записи блога. |
| [**`create_moderator_group.py`**](docs/api/create_moderator_group.md) | | |
| | [📦 Command](docs/api/create_moderator_group.md#Command) | Создаёт группу «Модератор продуктов» и назначает ей права. |
| | [⚙️ Command.add_arguments](docs/api/create_moderator_group.md#Command.add_arguments) | Добавляет аргументы командной строки. |
| | [⚙️ Command.handle](docs/api/create_moderator_group.md#Command.handle) | Создаёт группу и назначает ей права на товары и категории. |
| | [🔧 add_arguments](docs/api/create_moderator_group.md#add_arguments) | Добавляет аргументы командной строки. |
| | [🔧 handle](docs/api/create_moderator_group.md#handle) | Создаёт группу и назначает ей права на товары и категории. |
| [**`dell_all.py`**](docs/api/dell_all.md) | | |
| | [📦 Command](docs/api/dell_all.md#Command) | Команда удаления. |
| | [⚙️ Command.handle](docs/api/dell_all.md#Command.handle) | Хендл. |
| | [🔧 handle](docs/api/dell_all.md#handle) | Хендл. |
| [**`forms.py`**](docs/api/forms.md) | | |
| | [📦 CategoryForm](docs/api/forms.md#CategoryForm) | Форма для создания и редактирования категории. |
| | [📦 ProductForm](docs/api/forms.md#ProductForm) | Форма для создания и редактирования товара. |
| | [⚙️ ProductForm.clean_price](docs/api/forms.md#ProductForm.clean_price) | Проверяет, что цена больше 0. |
| | [⚙️ ProductForm.clean_image](docs/api/forms.md#ProductForm.clean_image) | Проверяет, что размер изображение не больше 0.5MB. И тип JPG, PNG, WEBP. |
| | [⚙️ ProductForm.clean_name](docs/api/forms.md#ProductForm.clean_name) | Проверяет, что имя не содержит запрещённые слова. |
| | [⚙️ ProductForm.clean_description](docs/api/forms.md#ProductForm.clean_description) | Проверяет, что описание не содержит запрещённые слова. |
| | [📦 Meta](docs/api/forms.md#Meta) | Внутренний класс с настройками формы. |
| | [📦 Meta](docs/api/forms.md#Meta) | Внутренний класс с настройками формы. |
| | [🔧 clean_price](docs/api/forms.md#clean_price) | Проверяет, что цена больше 0. |
| | [🔧 clean_image](docs/api/forms.md#clean_image) | Проверяет, что размер изображение не больше 0.5MB. И тип JPG, PNG, WEBP. |
| | [🔧 clean_name](docs/api/forms.md#clean_name) | Проверяет, что имя не содержит запрещённые слова. |
| | [🔧 clean_description](docs/api/forms.md#clean_description) | Проверяет, что описание не содержит запрещённые слова. |
| | [📦 BlogPostForm](docs/api/forms.md#BlogPostForm) | Форма для создания и редактирования записи блога. |
| | [⚙️ BlogPostForm.clean_preview](docs/api/forms.md#BlogPostForm.clean_preview) | Проверяет, что размер изображение не больше 0.5MB. И тип JPG, PNG, WEBP. |
| | [📦 Meta](docs/api/forms.md#Meta) | Внутренний класс с настройками формы. |
| | [🔧 clean_preview](docs/api/forms.md#clean_preview) | Проверяет, что размер изображение не больше 0.5MB. И тип JPG, PNG, WEBP. |
| | [📦 CustomUserCreationForm](docs/api/forms.md#CustomUserCreationForm) | Форма регистрации нового пользователя. |
| | [⚙️ CustomUserCreationForm.clean_email](docs/api/forms.md#CustomUserCreationForm.clean_email) | Проверяет, что email ещё не занят. |
| | [📦 CustomAuthenticationForm](docs/api/forms.md#CustomAuthenticationForm) | Форма авторизации по email и паролю. |
| | [📦 CustomUserChangeForm](docs/api/forms.md#CustomUserChangeForm) | Форма редактирования профиля пользователя. |
| | [📦 CustomPasswordChangeForm](docs/api/forms.md#CustomPasswordChangeForm) | Форма смены пароля с Bootstrap-стилями. |
| | [📦 Meta](docs/api/forms.md#Meta) | Внутренний класс с настройками формы. |
| | [🔧 clean_email](docs/api/forms.md#clean_email) | Проверяет, что email ещё не занят. |
| | [📦 Meta](docs/api/forms.md#Meta) | Внутренний класс с настройками формы. |
| [**`manage.py`**](docs/api/manage.md) | | |
| | [🔧 main](docs/api/manage.md#main) | Run administrative tasks. |
| [**`managers.py`**](docs/api/managers.md) | | |
| | [📦 CustomUserManager](docs/api/managers.md#CustomUserManager) | Менеджер пользователей, использующий email вместо username. |
| | [⚙️ CustomUserManager.create_user](docs/api/managers.md#CustomUserManager.create_user) | Создаёт и сохраняет обычного пользователя. |
| | [⚙️ CustomUserManager.create_superuser](docs/api/managers.md#CustomUserManager.create_superuser) | Создаёт и сохраняет суперпользователя. |
| | [🔧 create_user](docs/api/managers.md#create_user) | Создаёт и сохраняет обычного пользователя. |
| | [🔧 create_superuser](docs/api/managers.md#create_superuser) | Создаёт и сохраняет суперпользователя. |
| [**`mixins.py`**](docs/api/mixins.md) | | |
| | [📦 BootstrapStyleMixin](docs/api/mixins.md#BootstrapStyleMixin) | Миксин для стилизации полей формы под Bootstrap. |
| [**`models.py`**](docs/api/models.md) | | |
| | [📦 Category](docs/api/models.md#Category) | Модель категории товаров. |
| | [📦 Product](docs/api/models.md#Product) | Модель товара. |
| | [📦 Contact](docs/api/models.md#Contact) | Модель контактных данных компании. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета для админки. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета для админки. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета для админки. |
| | [📦 BlogPost](docs/api/models.md#BlogPost) | Модель записи в блоге. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета-параметры модели BlogPost. |
| | [📦 CustomUser](docs/api/models.md#CustomUser) | Кастомная модель пользователя. |
| | [📦 Meta](docs/api/models.md#Meta) | Мета-параметры модели CustomUser. |
| [**`seed_db.py`**](docs/api/seed_db.md) | | |
| | [📦 Command](docs/api/seed_db.md#Command) | Команда засеивания базы тестовыми данными. |
| | [⚙️ Command.handle](docs/api/seed_db.md#Command.handle) | Хенндл. |
| | [🔧 handle](docs/api/seed_db.md#handle) | Хенндл. |
| [**`validators.py`**](docs/api/validators.md) | | |
| | [🔧 validate_image_file](docs/api/validators.md#validate_image_file) | Проверяет размер и формат загружаемого изображения. |
| [**`views.py`**](docs/api/views.md) | | |
| | [📦 ProductListView](docs/api/views.md#ProductListView) | Представление для отображения списка товаров с пагинацией. |
| | [⚙️ ProductListView.get_queryset](docs/api/views.md#ProductListView.get_queryset) | Возвращает список товаров, при необходимости отфильтрованный по категории. |
| | [📦 ProductDetailView](docs/api/views.md#ProductDetailView) | Представление для отображения товара. |
| | [⚙️ ProductDetailView.get_queryset](docs/api/views.md#ProductDetailView.get_queryset) | Возвращает набор товаров, доступных текущему пользователю. |
| | [📦 ContactsView](docs/api/views.md#ContactsView) | Отображает страницу контактов и обрабатывает форму обратной связи. |
| | [⚙️ ContactsView.get](docs/api/views.md#ContactsView.get) | Получение данных о контакте для связи. |
| | [⚙️ ContactsView.post](docs/api/views.md#ContactsView.post) | Отправка обратной связи. |
| | [📦 ProductCreateView](docs/api/views.md#ProductCreateView) | Представление для добавления товара. |
| | [⚙️ ProductCreateView.get_success_url](docs/api/views.md#ProductCreateView.get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [⚙️ ProductCreateView.form_valid](docs/api/views.md#ProductCreateView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 CategoryCreateView](docs/api/views.md#CategoryCreateView) | Представление для добавления категории. |
| | [⚙️ CategoryCreateView.get_success_url](docs/api/views.md#CategoryCreateView.get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [⚙️ CategoryCreateView.form_valid](docs/api/views.md#CategoryCreateView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 ProductUpdateView](docs/api/views.md#ProductUpdateView) | Представление для редактирования товара. |
| | [⚙️ ProductUpdateView.get_queryset](docs/api/views.md#ProductUpdateView.get_queryset) | Возвращает товары, которые текущий пользователь может редактировать. |
| | [⚙️ ProductUpdateView.get_success_url](docs/api/views.md#ProductUpdateView.get_success_url) | Возвращает URL для перенаправления после успешного редактирования. |
| | [⚙️ ProductUpdateView.form_valid](docs/api/views.md#ProductUpdateView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 ProductDeleteView](docs/api/views.md#ProductDeleteView) | Представление для удаления товара. |
| | [⚙️ ProductDeleteView.get_queryset](docs/api/views.md#ProductDeleteView.get_queryset) | Возвращает товары, которые текущий пользователь может удалить. |
| | [⚙️ ProductDeleteView.form_valid](docs/api/views.md#ProductDeleteView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 ProductUnpublishView](docs/api/views.md#ProductUnpublishView) | Представление для снятия товара с публикации. |
| | [⚙️ ProductUnpublishView.get](docs/api/views.md#ProductUnpublishView.get) | Отображает страницу подтверждения снятия товара с публикации. |
| | [⚙️ ProductUnpublishView.post](docs/api/views.md#ProductUnpublishView.post) | Снимает товар с публикации и перенаправляет на страницу товара. |
| | [📦 CategoryUpdateView](docs/api/views.md#CategoryUpdateView) | Представление для редактирования категории. |
| | [⚙️ CategoryUpdateView.get_success_url](docs/api/views.md#CategoryUpdateView.get_success_url) | Возвращает URL для перенаправления после успешного редактирования. |
| | [⚙️ CategoryUpdateView.form_valid](docs/api/views.md#CategoryUpdateView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 CategoryDeleteView](docs/api/views.md#CategoryDeleteView) | Представление для удаления категории. |
| | [⚙️ CategoryDeleteView.form_valid](docs/api/views.md#CategoryDeleteView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 CategoryListView](docs/api/views.md#CategoryListView) | Представление для отображения списка категорий. |
| | [⚙️ CategoryListView.get_queryset](docs/api/views.md#CategoryListView.get_queryset) | Возвращает категории с подсчётом количества товаров. |
| | [🔧 get_queryset](docs/api/views.md#get_queryset) | Возвращает список товаров, при необходимости отфильтрованный по категории. |
| | [🔧 get_queryset](docs/api/views.md#get_queryset) | Возвращает набор товаров, доступных текущему пользователю. |
| | [🔧 get](docs/api/views.md#get) | Получение данных о контакте для связи. |
| | [🔧 post](docs/api/views.md#post) | Отправка обратной связи. |
| | [🔧 get_success_url](docs/api/views.md#get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 get_success_url](docs/api/views.md#get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 get_queryset](docs/api/views.md#get_queryset) | Возвращает товары, которые текущий пользователь может редактировать. |
| | [🔧 get_success_url](docs/api/views.md#get_success_url) | Возвращает URL для перенаправления после успешного редактирования. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 get_queryset](docs/api/views.md#get_queryset) | Возвращает товары, которые текущий пользователь может удалить. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 get](docs/api/views.md#get) | Отображает страницу подтверждения снятия товара с публикации. |
| | [🔧 post](docs/api/views.md#post) | Снимает товар с публикации и перенаправляет на страницу товара. |
| | [🔧 get_success_url](docs/api/views.md#get_success_url) | Возвращает URL для перенаправления после успешного редактирования. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 get_queryset](docs/api/views.md#get_queryset) | Возвращает категории с подсчётом количества товаров. |
| | [📦 BlogPostDetailView](docs/api/views.md#BlogPostDetailView) | Представление для отображения записи. |
| | [⚙️ BlogPostDetailView.get_queryset](docs/api/views.md#BlogPostDetailView.get_queryset) | Возвращает набор записей, доступных текущему пользователю. |
| | [⚙️ BlogPostDetailView.get_object](docs/api/views.md#BlogPostDetailView.get_object) | Переопредение данных записи, для увеличения счётчика просмотров. |
| | [⚙️ BlogPostDetailView.send_congratulation_email](docs/api/views.md#BlogPostDetailView.send_congratulation_email) | Отправляет поздравление о достижении 100 просмотров. |
| | [📦 BlogPostListView](docs/api/views.md#BlogPostListView) | Представление для отображения списка записей в блоге. |
| | [⚙️ BlogPostListView.get_queryset](docs/api/views.md#BlogPostListView.get_queryset) | Возвращает отсортированный список записей. |
| | [📦 BlogPostMyListView](docs/api/views.md#BlogPostMyListView) | Представление для отображения записей, созданных текущим пользователем. |
| | [⚙️ BlogPostMyListView.get_queryset](docs/api/views.md#BlogPostMyListView.get_queryset) | Возвращает записи текущего пользователя. |
| | [📦 BlogPostCreateView](docs/api/views.md#BlogPostCreateView) | Представление для добавления записи блога. |
| | [⚙️ BlogPostCreateView.get_success_url](docs/api/views.md#BlogPostCreateView.get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [⚙️ BlogPostCreateView.form_valid](docs/api/views.md#BlogPostCreateView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 BlogPostUpdateView](docs/api/views.md#BlogPostUpdateView) | Представление для редактирования записи блога. |
| | [⚙️ BlogPostUpdateView.get_success_url](docs/api/views.md#BlogPostUpdateView.get_success_url) | Возвращает URL для перенаправления после успешного редактирования. |
| | [⚙️ BlogPostUpdateView.form_valid](docs/api/views.md#BlogPostUpdateView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 BlogPostDeleteView](docs/api/views.md#BlogPostDeleteView) | Представление для удаления записи блога. |
| | [⚙️ BlogPostDeleteView.form_valid](docs/api/views.md#BlogPostDeleteView.form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 get_queryset](docs/api/views.md#get_queryset) | Возвращает набор записей, доступных текущему пользователю. |
| | [🔧 get_object](docs/api/views.md#get_object) | Переопредение данных записи, для увеличения счётчика просмотров. |
| | [🔧 send_congratulation_email](docs/api/views.md#send_congratulation_email) | Отправляет поздравление о достижении 100 просмотров. |
| | [🔧 get_queryset](docs/api/views.md#get_queryset) | Возвращает отсортированный список записей. |
| | [🔧 get_queryset](docs/api/views.md#get_queryset) | Возвращает записи текущего пользователя. |
| | [🔧 get_success_url](docs/api/views.md#get_success_url) | Возвращает URL для перенаправления после успешного создания. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 get_success_url](docs/api/views.md#get_success_url) | Возвращает URL для перенаправления после успешного редактирования. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Обрабатывает валидную форму и добавляет сообщение об успехе. |
| | [📦 RegisterView](docs/api/views.md#RegisterView) | Регистрация нового пользователя. |
| | [⚙️ RegisterView.form_valid](docs/api/views.md#RegisterView.form_valid) | Сохраняет пользователя и отправляет письмо с токеном активации. |
| | [⚙️ RegisterView.send_activation_email](docs/api/views.md#RegisterView.send_activation_email) | Отправляет письмо со ссылкой активации. |
| | [📦 ActivationSentView](docs/api/views.md#ActivationSentView) | Страница «проверьте почту» после регистрации. |
| | [⚙️ ActivationSentView.get](docs/api/views.md#ActivationSentView.get) | Отображает страницу с инструкцией. |
| | [📦 ActivateView](docs/api/views.md#ActivateView) | Активация аккаунта по ссылке из письма. |
| | [⚙️ ActivateView.get](docs/api/views.md#ActivateView.get) | Обрабатывает переход по ссылке активации. |
| | [📦 CustomLoginView](docs/api/views.md#CustomLoginView) | Авторизация пользователя по email и паролю. |
| | [📦 CustomLogoutView](docs/api/views.md#CustomLogoutView) | Выход пользователя из системы. |
| | [📦 ProfileDetailView](docs/api/views.md#ProfileDetailView) | Просмотр профиля текущего пользователя. |
| | [⚙️ ProfileDetailView.get_object](docs/api/views.md#ProfileDetailView.get_object) | Возвращает текущего пользователя. |
| | [📦 ProfileUpdateView](docs/api/views.md#ProfileUpdateView) | Редактирование профиля текущего пользователя. |
| | [⚙️ ProfileUpdateView.get_object](docs/api/views.md#ProfileUpdateView.get_object) | Возвращает текущего пользователя. |
| | [⚙️ ProfileUpdateView.form_valid](docs/api/views.md#ProfileUpdateView.form_valid) | Сохраняет профиль и добавляет сообщение об успехе. |
| | [📦 CustomPasswordChangeView](docs/api/views.md#CustomPasswordChangeView) | Смена пароля текущего пользователя. |
| | [⚙️ CustomPasswordChangeView.form_valid](docs/api/views.md#CustomPasswordChangeView.form_valid) | Сохраняет новый пароль и добавляет сообщение об успехе. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Сохраняет пользователя и отправляет письмо с токеном активации. |
| | [🔧 send_activation_email](docs/api/views.md#send_activation_email) | Отправляет письмо со ссылкой активации. |
| | [🔧 get](docs/api/views.md#get) | Отображает страницу с инструкцией. |
| | [🔧 get](docs/api/views.md#get) | Обрабатывает переход по ссылке активации. |
| | [🔧 get_object](docs/api/views.md#get_object) | Возвращает текущего пользователя. |
| | [🔧 get_object](docs/api/views.md#get_object) | Возвращает текущего пользователя. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Сохраняет профиль и добавляет сообщение об успехе. |
| | [🔧 form_valid](docs/api/views.md#form_valid) | Сохраняет новый пароль и добавляет сообщение об успехе. |

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
- [x] Приложение users с URL-роутингом
- [x] Кастомная модель `CustomUser` на базе `AbstractUser` с email как `USERNAME_FIELD`
- [x] Дополнительные поля пользователя: аватар, телефон, страна
- [x] Кастомный менеджер `CustomUserManager` для создания пользователей по email
- [x] Настройка админки для `CustomUser`
- [x] Форма регистрации с подтверждением пароля и валидацией email
- [x] Активация аккаунта по email через токен
- [x] Отправка приветственного письма после регистрации
- [x] Авторизация по email и паролю
- [x] Выход из системы через POST-форму
- [x] Закрытие CUD товаров и категорий для анонимных пользователей (`LoginRequiredMixin`)
- [x] Страница списка категорий с количеством товаров
- [x] Фильтрация товаров по категории
- [x] Редактирование и удаление товаров
- [x] Редактирование и удаление категорий
- [x] Редактирование и удаление записей блога
- [x] Dropdown-меню пользователя в навбаре
- [x] Просмотр профиля пользователя
- [x] Редактирование профиля пользователя
- [x] Смена пароля
- [x] Проверить линтеры (`ruff`, `mypy`)
- [x] Финальная вычитка документации и обновление README
- [x] Обновить документацию
- [x] Роли и группы прав: «Модератор продуктов», «Контент-менеджер», команды выдачи
- [x] Владельцы товаров и записей блога, страница «Мои записи»
- [x] Снятие товара с публикации через кастомное право `can_unpublish_product`
- [x] Ограничение CRUD категорий на модератора продуктов и суперпользователя
- [x] Выдача `is_staff` ролевым пользователям, фикстуры пользователей и записей блога

## Команда проекта

- Matvey Bakirov — [mabakirov@gmail.com](mailto:mabakirov@gmail.com) — Back-End Engineer
