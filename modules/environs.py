from environs import Env

env = Env()
env.read_env()

FTP_HOST = env.str("FTP_HOST")
FTP_USER = env.str("FTP_USER_NAME")
FTP_PASSWORD = env.str("FTP_PASSWORD")
FTP_CWD = env.str("FTP_CWD")