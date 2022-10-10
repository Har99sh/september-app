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

pip install flask flask-cors flask_login sqlite3 psycopg2 python-decouple python-dotenv selenium


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
    flask-jwt-extended

**Database:**

    sqlite3
    psycopg2

**Vue**

    axios
    vue-router
    bootstrap-vue
    bootstrap
    pinia
    jwt-decode





In the root of project, create .env file with the following variables

    SECRET_KEY = 'generate your secret key'

    PGSQL_HOST = "localhost"
    PGSQL_USER = 'your_user'
    PGSQL_PASSWORD = 'your_password'
    PGSQL_DATABASE  = 'db_just_4_work'
    PGSQL_PORT = 5414   your port

    JWT_KEY = 'generate key'



<h3>Vue dependencies</h3>

Enter your root project folder  (carpeta raíz del proyecto)


in console 

    cd webapp/ 
    npm install 
    npm run serve


<h3>Flask dependencies</h3>

in console

    cd backend
    / activate venv command for your os/
    pip3 (or pip) install -r requirements.txt
en caso de error OPENSSL_CONF (windows), hay que poner el siguiente comando en la terminal de venv (activada) y en la terminal de la webapp antes de hacer npm install : 

    set OPENSSL_CONF=
