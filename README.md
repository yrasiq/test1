Версия Python - 3.9.1

Запуск:
1. Перейти в консоли в корневой каталог
2. Создать виртуальное окружение: python -m venv venv
3. Войти в виртуальное окружение: Linux: source venv/bin/activate, Windows: venv\Scripts\activate
4. Установить зависимости из requirements.txt: python -m pip install -r requirements.txt
5. Провести миграции БД: python cities/manage.py migrate

Заполнение БД тестовыми данными: python cities/manage.py data (только для пустой БД).
