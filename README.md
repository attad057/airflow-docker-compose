# airflow-docker-compose

# Features
**1.** Docker compose setup with the Airflow webserver, scheduler, a celery worker, celery flower, postgre sql, pgadmin and redis as services
**2.** Redis as the celery broker
**3.** Postgres, Pgadmin and airflow configuration saved in the .env file
**4.** One-time init script to initialize the database and create a default user
**3.** Dags are setup as a volume in /dags, update dags in this local folder to automatically sync to docker
**4.** Logs are setup as a volume in /logs-volume. View services logs in this local folder
**5*.** Postgre database is peristed in a docker volume: database-data, so that the database data won't depend on the container.


### How to set-up:

**1.**: Install Docker and docker-compose. 

**2:** Clone this Repo.

**2:** Go through .env file, init_airflow_setup.sh, docker-compose.yml file to change settings as preferred

**Step 3:** Open cmd terminal and run `docker-compose up -d --remove-orphans`

**Step 4:** Run `scripts/init-airflow-setup.bat` (Only for initial deployment)

**Step 5:** Go to http://localhost:8080 and login with user: _airflow_test_user_ and password: _airflow_test_password_ as specified in init_airflow_setup.sh script

**Step 6:** Run few dags and monitor Celery workers at http://localhost:5555

**Step 7:** Access the airflow database with Pgadmin at http://localhost:80 to create database objects


