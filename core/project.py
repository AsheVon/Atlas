from dataclasses import dataclass
from pathlib import Path


@dataclass
class Project:

    name: str

    location: Path

    template: str