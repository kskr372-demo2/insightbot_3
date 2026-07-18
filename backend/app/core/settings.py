

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application Settings
    """

    app_name: str = "InsightBot API"
    app_version: str = "0.1.0"
    app_environment: str = "developmentttt"
    api_prefix: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )
    gemini_api_key: str
    gemini_model: str

settings = Settings()