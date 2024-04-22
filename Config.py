import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
    INSTA_USERNAME = os.environ.get('INSTA_USERNAME', None)
    INSTA_PASSWORD = os.environ.get('INSTA_PASSWORD', None)
else:
    # Fill the Values
    API_ID = 10471716
    API_HASH = "f8a1b21a13af154596e2ff5bed164860"
    BOT_TOKEN = "6999401413:AAHgF1ZpUsCT5MgWX1Wky7GbegyeHvzi2AU"
    DATABASE_URL = "mongodb+srv://appuz:chrijismiappuz@cluster0.yngvhc2.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "botio_devs"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
    INSTA_USERNAME = "botio_devs"
    INSTA_PASSWORD = "Appus123/"
