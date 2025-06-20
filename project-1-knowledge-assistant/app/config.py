from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # MongoDB
    MONGO_URI: str
    MONGO_DB: str
    # Waviate
    WEAVIATE_URL: str
    # LLM
    MODEL_NAME: str
    OPENAI_API_KEY: str
    # Chunking
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    class Config:
        env_file = ".env"


settings = Settings()
