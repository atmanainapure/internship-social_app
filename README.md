# internship-social_app
social media backend using flask and postgresql

# requirements.txt
Download all the requirements from the requirements.txt
```bash
pip install requirements.txt
```
# app.py
Run the app.py

```bash
python app.py
```
# PostgreSQL
I used pgadmin as the GUI for PostgreSQL.
# URI for PostgreSQL
For creating the URI for PostgreSQL, do the following:
-specify your username, your password, your port and your database name.
```bash
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@host:5724/database_name'

```
# make a .env file in the current directory to specify the username, password etc. 
For example:
POSTGRES_USER="Atman"
POSTGRES_PASSWORD="temp1234"
POSTGRES_DB="postgres123"

# Docker commands:
```bash
docker compose --env-file ./.env -d up postgres-dev-db
docker compose rm -s -f -v postgres-dev-db
```
