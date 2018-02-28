import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '')
DB_DRIVER = os.environ.get('DB_DRIVER', 'postgres')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', 5432)
DB_USER = os.environ.get('DB_USER', '')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_NAME = os.environ.get('DB_NAME', '')
