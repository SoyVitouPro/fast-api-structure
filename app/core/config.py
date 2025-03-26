from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FASTAPI"
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "rdlab123"
    MYSQL_DATABASE: str = "fastapi_db"
    MYSQL_PORT: int = 3306
    DB_HOST: str = "127.0.0.1"
    DB_DRIVER: str = "mysql+aiomysql"

    @property
    def DATABASE_URL(self) -> str:
        return f"{self.DB_DRIVER}://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.DB_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"


settings = Settings()
