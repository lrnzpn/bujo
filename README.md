# Bujo V1

## How to start

```bash
# clone the repository and switch to lab directory
# this command should be able to clone the repository and switch to the lab2 branch
$ git clone -b lab2 https://gitlab.discs.ateneo.edu/miggypinaroc/pinaroc_lab1.git && cd pinaroc_lab1/

# create virtualenv
$ virtualenv env && source env/bin/activate

# install dependencies from requirements.txt
$ pip install -r requirements.txt

# create .env file for postgres credentials (check .sample.env)
$ touch bujov1/.env

# make migrations and migrate changes
$ python manage.py makemigrations
$ python manage.py migrate

# start the server
$ python manage.py runserver

```