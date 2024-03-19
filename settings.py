from os import (
    path,
    environ,
)

DIR_PATH: str = path.dirname(path.realpath(__file__))

POSTGRES_USER: str = environ.get('POSTGRES_USER', default='developer')
POSTGRES_PASSWORD: str = environ.get('POSTGRES_PASSWORD', default='developer')
POSTGRES_HOST: str = environ.get('POSTGRES_HOST', default='localhost')
POSTGRES_PORT: str = environ.get('POSTGRES_PORT', default='5432')
POSTGRES_DB: str = environ.get('POSTGRES_DB', default='developer')

DATA_BASE_URL: str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'


SKIP_SHEETS: set = {'задача'}
