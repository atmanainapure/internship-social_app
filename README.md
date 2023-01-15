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

# .env
make a .env file in the current directory to specify the username, password etc. 
For example write this in the .env file:
POSTGRES_USER="Atman"
POSTGRES_PASSWORD="temp1234"
POSTGRES_DB="postgres123"

# Docker commands:
Install docker desktop then run these commands in the current working directory:

```bash
docker compose --env-file ./.env -d up postgres-dev-db
docker compose rm -s -f -v postgres-dev-db
```
