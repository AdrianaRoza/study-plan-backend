from fastapi import BackgroundTasks
from pydantic_settings import BaseSettings

class EmailSettings(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_SERVER: str
    MAIL_PORT: int
    MAIL_FROM: str
    USE_CREDENTIALS: bool
    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool  

    class Config:
        env_file = ".env"

settings = EmailSettings()

def send_reset_email(email_to: str, background_tasks: BackgroundTasks):
    # Aqui vai o código para enviar o email
    pass
