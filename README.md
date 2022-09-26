# september-app
1) Dentro de la carpeta de backend crear la carpeta venv con el siguiende comando:

cd backend/ 

para LINUX/MAC: python3 -m venv venv

para WINDOWS: py -3 -m venv venv

2) Activar la carpeta anterior con el comando:
3) 
para LINUX: . venv/bin/activate
para WINDOWS: venv\Scripts\activate

3) Dentro del proyecto instalar flask y modulos que usaremos:

pip install flask flask-cors flask_login sqlite3 psycopg2 python-decouple python-dotenv


Dependencies
------------

**Python:**

    unicodedata
    uuid
    python-dotenv
    python-decouple


**Flask:**

    flask
    flask_login
    flask_cors
    werkzeug

**Database:**

    sqlite3
    psycopg2

**Vue**

    axios
    vue-router
    bootstrap-vue
    bootstrap



<h3>Database:</h3>

Download postgres, run an instance on your machine

in console

    $createdb db_just_4_work 

    $psql db_just_4_work < "COPY YOUR ROUTE TO THE FILE HERE"/september-app/pg_dump.sql

    


In the root of project, create .env file with the following variables

    SECRET_KEY = 'generate your secret key'

    PGSQL_HOST = "localhost"
    PGSQL_USER = 'your_user'
    PGSQL_PASSWORD = 'your_password'
    PGSQL_DATABASE  = 'db_just_4_work'

<h3>Vue dependencies</h3>

Enter your root project folder  (carpeta raíz del proyecto)


in console 

    cd webapp/ 
    npm install 
    npm run 