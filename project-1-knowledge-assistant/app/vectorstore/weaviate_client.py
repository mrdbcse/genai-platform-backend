from uuid import uuid4

import weaviate
from app.config import settings
from weaviate.embedded import EmbeddedOptions

client = weaviate.Client(
    url=settings.WEAVIATE_URL,
    additional_headers={"X-OpenAI-Api-Key": settings.OPENAI_API_KEY},
)

CLASS_NAME = "DocumentChunks"


def init_schema():
    if not client.schema.exists(CLASS_NAME):
        schema = {
            "class": CLASS_NAME,
            "vectorizer": "text2vec-openai",
            "properties": [
                {"name": "text", "dataType": ["text"]},
                {"name": "document_id", "dataType": ["text"]},
            ],
        }
        client.schema.create_class(schema)
    return
