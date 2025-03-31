from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    PORT: int = 8090
    MAX_USERS: int = 500
    HOST: str = "localhost"
    PROTOCOL: str = "http"

    # model_config = SettingsConfigDict(
    #    env_file=".env"
    #)

config_emulate = Config()

class ProjectKey(BaseModel):
    key: str

class IssueType(BaseModel):
    id: str

class IssueFields(BaseModel):
    summary: str
    description: str = ""
    project: ProjectKey
    issuetype: IssueType

class CreateIssue(BaseModel):
    fields: IssueFields


