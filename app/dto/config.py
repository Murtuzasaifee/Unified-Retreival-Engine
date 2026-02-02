"""Hydra configuration schemas using dataclasses."""

from dataclasses import dataclass
from typing import Optional

from hydra.core.config_store import ConfigStore


@dataclass
class AppConfig:
    """App configuration."""
    app_name: str
    app_version: str
    environment: str
    root_path: str
    upload_dir: str
    cache_dir: str

@dataclass
class OpenAIConfig:
    """OpenAI configuration."""
    api_key: str


@dataclass
class PineconeConfig:
    """Pinecone configuration."""
    environment: str
    api_key: str
    index_name: str


@dataclass
class DocumentProcessingConfig:
    """Document processing configuration."""
    chunk_size: int = 512
    chunk_overlap: int = 50
    min_chunk_overlap: int = 256
    use_docling: bool = True


@dataclass
class SupabaseConfig:
    """Supabase configuration."""
    database_url: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str


@dataclass
class LoggingConfig:
    """Logging configuration."""
    level: str = "INFO"


@dataclass
class OpikConfig:
    """Opik configuration."""
    api_key: str
    project_name: str

@dataclass
class VannaConfig:
    """Vanna configuration."""
    vanna_model: str
    vanna_pinecone_index: str
    vanna_namespace: str
    vanna_temperature: float
    vanna_top_p: float
    vanna_seed: int
    vanna_max_tokens: int

@dataclass
class StorageConfig:
    storage_backend: str
    s3_cache_bucket: str
    aws_region: str

@dataclass
class UpstashConfig:
    redis_url: str
    redis_token: str

@dataclass
class CacheConfig:
    ttl_embeddings: int
    ttl_rag: int
    ttl_sql_gen: int
    ttl_sql_result: int

@dataclass
class APIConfig:
    """API configuration."""
    host: str = "0.0.0.0"
    port: int = 8000


@dataclass
class AppConfig:
    """Main application configuration."""
    app: AppConfig
    openai: OpenAIConfig
    pinecone: PineconeConfig
    document_processing: DocumentProcessingConfig
    supabase: SupabaseConfig
    logging: LoggingConfig
    opik: OpikConfig
    vanna: VannaConfig
    api: APIConfig


def register_configs() -> None:
    """Register configuration schema with Hydra ConfigStore."""
    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=AppConfig)
