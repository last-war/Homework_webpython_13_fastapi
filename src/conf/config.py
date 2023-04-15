from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    mail_host_user: str
    mail_host_password: str
    mail_from: str = 'PythonStudent@meta.ua'
    mail_from_name: str = 'PythonStudent'
    mail_port: int
    mail_host: str
    redis_host: str = 'localhost'
    redis_port: int = 6379

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

