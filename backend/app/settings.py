from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Config de entorno. Carga de variables y opcionalmente .env."""

    DATABASE_URL: str = "postgresql+psycopg2://camion:camion@localhost:5432/camion"
    MAPS_PROVIDER: str = "google"
    JWT_SECRET: str = "change-me"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
