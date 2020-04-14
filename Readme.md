Projeto migrado para [novo repositório](https://gitlab.com/devopspbs/django/covid-19)

Repositorio do projeto DevOpsPBS Covid-19, o objetivo to projeto é criar um dash board com dados importanteste sobre a epidemia do covid-19 e de recursos em saúde, e monitorlos diaramente, para ajudar na tomada de decisões dos getores municipais.

## Pre-requisitos:
- Conhecimentos básico de python 3, Django3 e Django Rest Framework
- docker run
- docker composer

## Back-end:
### Start in standalone mode:
- `docker-compose run --service-ports --rm django /bin/bash`

## Django start:
- ./manager.py migrate
- ./manager.py createsuperuser
- ./manager.py runserver 0:8000

## Bonus:
### Carrega os dados do estado do Pará
- ./manager.py loaddata --app covid19 dumps/Covid19_PA_UP_31_03_2020_dump.json

## Help's
### Acesse psql prompt
- `docker exec -it postgres psql -U postgres`
### Make a dump
- `docker exec <postgres_container_name> pg_dump -U postgres <database_name> > backup.sql`
### E.G.
- `docker exec docker-composer_postgres-db_1 pg_dump -U teste teste > backup.sql`
### Make a restau
- `docker exec -i <postgres_container_name> psql -U postgres -d <database_name> < backup.sql`
### E.G.
- `docker exec -i docker-composer_postgres-db_1 psql -U teste -d teste < Cloud_SQL_Export_2020-02-22.dump`

## OBS:

## Creditos
- https://github.com/chandez/Estados-Cidades-IBGE
- https://servicodados.ibge.gov.br/api/docs/localidades

## Referencias

Docker-compose:
https://medium.com/@renato.groffe/postgresql-pgadmin-4-docker-compose-montando-rapidamente-um-ambiente-para-uso-55a2ab230b89

