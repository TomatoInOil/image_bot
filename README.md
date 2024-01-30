# image_bot
I'm trying to handle multiple images in PTB

## Требования
1. Токен Telegram бота
2. Poetry

## Запуск проекта в режиме разработки
1. Заполнить `.env` по образцу `.env.example`
2. Установить зависимости с помощью poetry
    ```shell
    poetry install
    ```
3. Запустить backend
    ```shell
    cd src/
    python manage.py runserver
    ```
4. Запустить бота в новом терминале
    ```shell
    cd src/
    python run_bot.py
    ```
   
### Работа с ботом
После запуска в боте доступна обработка команды `/photo`