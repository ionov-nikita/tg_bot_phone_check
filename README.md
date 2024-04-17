#Telegram bot

## Описание

Телеграм бот определяет по номеру телефона следующие параметры:
* Тип телефона
* Регион
* Страну
* Код страны
* Префикс страны
* Оператора

## Установка и запуск

1. Склонируйте репозиторий:
 ```ssh
 git@github.com:ionov-nikita/tg_bot_phone_check
 ```
2. Активируйте виртуальное окружение:
 ```sh
  source venv/bin/activate
  ```
3. Установите зависимости:
 ```sh
  pip install -r requirements.txt
 ```
4. Запустите проект:
 ```sh
  python3 bot.py
 ```

## Полезные ссылки

* https://veriphone.io/docs/v2
