from pathlib import Path
from core.logger import AtlasLogger


class FolderBuilder:
    """Creates the folder hierarchy defined in a template."""

    def __init__(self):
        self.logger = AtlasLogger()

    def create(self, project_path: Path, template: dict):
        folders = template.get("folders", [])

        self.logger.section("Creating Folder Structure")

        for folder in folders:
            current = project_path / Path(folder)
            current.mkdir(parents=True, exist_ok=True)
            self.logger.success(folder)

        self.logger.info("\nFolder creation complete.")