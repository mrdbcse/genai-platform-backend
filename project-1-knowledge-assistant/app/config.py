from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    MONGO_URI: str
    MODEL_NAME: str
    WEAVIATE_URL: str
    MONGO_DB_NAME: str
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    class Config:
        env_file = ".env"


settings = Settings()
