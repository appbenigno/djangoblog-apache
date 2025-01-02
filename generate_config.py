import secrets, json

FILE_NAME = '/etc/config-django.json'

SECRET_KEY = secrets.token_hex(nbytes=32)
DATABASE_URI = "db.sqlite3"
MAIL_USERNAME = input('Email: ')
MAIL_PASSWORD = input('App Password: ')
API_KEY = input('API_KEY: ')

data = {
    "SECRET_KEY": SECRET_KEY,
    "DATABASE_URI": DATABASE_URI,
    "EMAIL_USER": MAIL_USERNAME,
    "EMAIL_PASS": MAIL_PASSWORD,
    "API_KEY": API_KEY
}

with open(file=FILE_NAME, mode='w') as json_file:
    json.dump(data, json_file, indent=4)

print(f'Data has been written to: {FILE_NAME}')