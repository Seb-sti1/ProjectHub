"""Initialize the global settings and the global Config."""
from __future__ import annotations
from typing import Optional
from pathlib import Path
import json
#from getpass import getpass  # will be used to input tokens

from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ["Settings", "Config"]

DEFAULT_CONFIG_FILE = Path("~/.config/projecthub/core.json")
DOTENV_FILE = Path(__file__).with_name(".env")


class _Settings(BaseSettings):
    """Automatically loads the settings from a `.env` file.

    This is designed to be a Singleton instance. 
    The settings are loaded once and can then be accessed using the Setting instance.
    """

    model_config = SettingsConfigDict(env_file=DOTENV_FILE)

    # The Path does not necessary exists, use FilePath otherwise
    config_path: Path = Field(
        default=DEFAULT_CONFIG_FILE,
        description="The default path used to store the custom config file in a json format.",
        examples=[ Path("~/.config/projecthub/core.json") ],
    )

    @field_validator("config_path")
    @classmethod
    def validate_config_path(cls: type[_Settings], path: Path) -> Path:
        """Ensure that the path is not relative and expand the user if provided.
        The path as to be a json file."""

        if path.suffix != ".json":
            raise ValueError("The config file has to be a json file.")
        return path.expanduser().absolute()

Settings = _Settings()


class _Config(BaseModel):
    """Contains all the configurable fields in Project Hub.
    They can be edited by creating a json file in the `config_path` location.

    This is designed to be a Singleton instance. 
    The configurations are loaded once and can then be accessed using the Config instance.
    """

    dummy_field: str = Field(
        default="default value",
        description="Just a dummy field for the example",
        examples=["custom string"]
    )

    def __init__(self, config_file: Optional[Path]=None, **kwargs) -> None:

        # overwrite provided values by the ones in the config file if exists
        if config_file is not None and config_file.exists():
            kwargs |= json.loads(config_file.read_text(encoding="utf-8"))

        super().__init__(**kwargs)

Config = _Config(Settings.config_path)
