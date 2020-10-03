## Description

Simple web application example built with **Django** and **Elasticsearch** that searches for a **Digital library**:



### How to run

```bash
$ docker-compose up
```
### set up

```bash
$ docker run -e POSTGRES_USER=dchambers -e POSTGRES_PASSWORD=maestro -e POSTGRES_DB=searchx library/postgres

$ docker exec -it searchx_web_1 python ./manage.py createsuperuser
```