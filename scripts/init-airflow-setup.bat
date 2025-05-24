@echo off
REM WARNING: Run this script only during initial airflow db setup.

SET IS_INITDB=True
SET AIRFLOW_USER=airflow_test_user
SET AIRFLOW_PASSWORD=airflow_test_password
SET AIRFLOW_USER_EMAIL=airflow@airflow.com

IF "%IS_INITDB%"=="" GOTO SKIP_INIT

echo Initializing Airflow DB setup and Admin user setup because value of IS_INITDB is %IS_INITDB%
echo Airflow admin username will be %AIRFLOW_USER%

docker exec -ti airflow_cont airflow db init && echo Initialized airflow DB
docker exec -ti airflow_cont airflow users create --role Admin --username %AIRFLOW_USER% --password %AIRFLOW_PASSWORD% -e %AIRFLOW_USER_EMAIL% -f airflow -l airflow && echo Created airflow Initial admin user with username %AIRFLOW_USER%

GOTO END

:SKIP_INIT
echo Skipping InitDB and InitUser setup because value of IS_INITDB is %IS_INITDB%

:END