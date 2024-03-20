 # Nur-Telecom (Revenue Assurance Fraud Management)
 
## Задачи
Необходимо было обработать данные и решить следующие задачи:
* Загрузить в БД данные (любая СУБД на усмотрение);
* Написать скрипт для сверки данных.


## Краткое описание
Были 2 источника, ТИП_Источника_1 (source_1) и ТИП_Источника_2 (source_2). Сделал нормализацию: поработал над неймингами, стандартизировал по PEP. Загрузил данные из xlsx файла в БД(PostgreSQL). Сделал расчёт между данными source_1 и source_2, соединив их по TRANS_ID, отобразил их разницы. Подробно можно увидеть в [tasks_on_xlsx.ipynb](tasks_on_xlsx.ipynb) файле. Ответы на вопросы написаны [тут](task_on_questions)

## Результаты
source_1
![данные source_1 в БД](/source/source_1.png "Source_1")
source_2
![данные source_2 в БД](/source/source_2.png "Source_2")
inner join
![inner join](/source/overalll_data.png "Source_2")
разница
![difference](/source/actual_delta.png "Source_2")


## Используемые навыки и инструменты
`Python`, `Pandas`, `SQLalchemy`, `Анализ данных`, `предобработка данных (если так можно назвать)`, `Docker`, `Postgres`



# Инструкция по проекту

## Postgresql & PgAdmin


## Requirements:
* docker >= 17.12.0+
* docker-compose

## Quick Start
* клонировать данный репозиторий
* открыть проект в директории
* ранить эту команду `docker-compose up -d`


## Окружение

* `POSTGRES_USER` the default value is **developer**
* `POSTGRES_PASSWORD` the default value is **developer**
* `PGADMIN_PORT` the default value is **5050**
* `PGADMIN_DEFAULT_EMAIL` the default value is **developer@nurtelecom.kg**
* `PGADMIN_DEFAULT_PASSWORD` the default value is **developer**

## Postgres: 
* `localhost:5432`
* **Username:** developer или posgres
* **Password:** developer

## APgAdmin: 
* **URL:** `http://localhost:5050`
* **Username:** developer@nurtelecom.kg
* **Password:** developer

## Add a new server in PgAdmin:
* **Host name/address** `postgres`
* **Port** `5432`
* **Username** as `POSTGRES_USER`, by default: `developer`
* **Password** as `POSTGRES_PASSWORD`, by default `developer`