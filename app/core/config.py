from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./khyal.db"
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    s3_bucket_name: str = ""
    openai_api_key: str = ""
    elevenlabs_api_key: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
