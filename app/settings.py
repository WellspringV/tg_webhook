from environs import Env

env = Env()
env.read_env()


with env.prefixed("APP_"):
    SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI")
