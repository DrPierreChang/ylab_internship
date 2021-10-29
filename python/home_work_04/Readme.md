# Книга рецептов
Веб-сайт, использующий фреймворк Django 3.

В панели управления (/admin) пользователь имеет возможность ввести:

1. список ингредиентов для рецепта;

2. добавить текст и название рецепта.

В публичной части сайта пользователь
имеет возможность просмотра введенных рецептов
с выводом ингредиентов с возможностью фильтрации
по ингредиентам и названию рецепта.
Учтено, что один ингредиент может встречаться в нескольких рецептах.

Разработана схема базы данных,
описаны соответствующие модели для таблиц.
Таким образом, схема базы данных приведена к третьей нормальной форме (3НФ).

При первом запуске проекта
база данных наполняется данными благодаря миграции и добавлению фикстур.

Проект упакован в Docker (имеет Dockerfile и docker-compose.yml).

Для разработки проекта использовались:

1) СУБД PostgreSQL 14

2) Фреймворк Django 3.2.8

3) Python3.9

СУБД и веб-приложение запускаются в отдельных Docker-контейнерах.

### Инструкцией по запуску



### Создание виртуального окружения



```
python3.9 -m venv venv
```

### Установка Django 

```
python -m pip install Django
```

### Создание проекта
```
django-admin startproject app

```
### Создание приложения cookbook в директории проекта app
```shell
python manage.py startapp cookbook
```



# Источники информации

Документация

- [Django](https://www.djangoproject.com/)

Книги

- Использование Docker (Эдриен Моуэт)
- Two Scoops Of Django 3

StackOverflow
- [docker-compose gives ERROR: Cannot locate specified Dockerfile: Dockerfile](
  https://stackoverflow.com/questions/36236491/docker-compose-gives-error-cannot-locate-specified-dockerfile-dockerfile
  )
  
- [How do I get into a Docker container's shell?](
  https://stackoverflow.com/questions/30172605/how-do-i-get-into-a-docker-containers-shell
  )
  
- [How to remove old Docker containers](
  https://stackoverflow.com/questions/17236796/how-to-remove-old-docker-containers
  )

GitHub
- [Каталог Книг](https://github.com/MNV/django-booklist)

Хабр

- [Итерируемый объект, итератор и генератор](https://habr.com/ru/post/337314/)

YouTube

- [Setting up PostgreSQL database with a Django Docker application](
  https://youtu.be/610jg8bK0I8
  )
- [Docker | How to Dockerize a Django application (Beginners Guide)](
  https://youtu.be/W5Ov0H7E_o4
  )

Другое

- [requirements.txt — что это и зачем?](
  https://semakin.dev/2020/04/requirements_txt/)
  
- [OCI runtime exec failed: exec failed](
  https://www.reddit.com/r/docker/comments/fru7wp/oci_runtime_exec_failed_exec_failed/
  )

