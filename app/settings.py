from environs import Env

env = Env()
env.read_env()


with env.prefixed("BOT"):
    BOT_TOKEN = env.str("BOT_TOKEN")
