Repositorio do projeto DevOpsPBS Covid-19, o objetivo to projeto é criar um dash board com dados importanteste sobre a epidemia do covid-19 e de recursos em saúde, e monitorlos diaramente, para ajudar
na tomada de decisões dos getores municipais.

Start in standalone mode:
- `docker-compose run --service-ports --rm django /bin/bash`

## Help's
Acesse psql prompt
docker exec -it postgres psql -U postgres
Make a dump
`docker exec <postgres_container_name> pg_dump -U postgres <database_name> > backup.sql`
E.G.
`docker exec docker-composer_postgres-db_1 pg_dump -U teste teste > backup.sql`
Make a restau
`docker exec -i <postgres_container_name> psql -U postgres -d <database_name> < backup.sql`
E.G.
`docker exec -i docker-composer_postgres-db_1 psql -U teste -d teste < Cloud_SQL_Export_2020-02-22.dump`

## OBS:

## Creditos
- https://github.com/chandez/Estados-Cidades-IBGE
- https://servicodados.ibge.gov.br/api/docs/localidades

## Referencias

Docker-compose:
https://medium.com/@renato.groffe/postgresql-pgadmin-4-docker-compose-montando-rapidamente-um-ambiente-para-uso-55a2ab230b89