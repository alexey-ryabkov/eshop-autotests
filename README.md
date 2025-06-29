# Итоговая работа по курсу "Модульное тестирование веб-приложений" в ITHub

В рамках итоговой работы протестирован с использованием pytest-playwright интернет-магазин Opencart в докер-образе

## Подготовка и запуск тестов

Для развертывания проекта в системе должены быть установлены Python 3 и Docker 

### Развертывание проекта

Выполнить последовательно
```bash
# установка менеджера зависимостей Poetry (если не установлен)
curl -sSL https://install.python-poetry.org | python3 -
# установка необходимых пакетов проекта
poetry install --no-root
```

Далее необходимо создать файл .env с параметрами для докер-образа, см. [.env.sample](/.env.sample)

### Запуск тестов

При запуске тестов докер-образ запустится автоматически.
```bash
poetry run pytest
# если нужно предотвратить завершение работы докера по окончании тестов
poetry run pytest --keep-docker
```

## Отчет Allure

Команда для формирование отчета по тестам (в системе должен быть установлен Allure):
```bash
poetry run pytest --alluredir=allure_results && allure generate allure_results -o report --clean 
# для просмотра на локальном веб-сервере выполнить 
poetry run python -m http.server --directory report 8080 
```
