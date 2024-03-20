from __future__ import annotations
from pathlib import Path
#from getpass import getpass  # will be used to input tokens

from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings

__all__ = ["Settings", "Config"]

DEFAULT_CONFIG_FILE = Path("~/.config/projecthub/core.json")


class _Settings(BaseSettings):
    """Automatically loads the settings from a `.env` file.

    This is designed to be a Singleton instance. 
    The settings are loaded once and can then be accessed using the Setting instance.
    """

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

    def __init__(self) -> None:
        # TODO: load the configurations from the config file in kwargs if the file exists.
        kwargs = {}
        super().__init__(**kwargs)

Config = _Config()
