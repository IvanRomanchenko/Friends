# Friends
#### _App for friends_  

## Start:
```sh
git clone https://github.com/IvanRomanchenko/Friends.git
cd Friends/app
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
createdb -U postgres Friends_db
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata data.yaml
```

## Usage

```sh
python manage.py runserver
```
