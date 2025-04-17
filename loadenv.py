import os, dotenv

def load_env():
    PATH_ENV = os.path.abspath(os.path.join(__file__, '..', '.env'))

    dotenv.load_dotenv(dotenv_path= PATH_ENV)

    os.system(os.environ['DB_MIGRATIONS_DIR'])
    os.system(os.environ['DB_MIGRATE'])

load_env()