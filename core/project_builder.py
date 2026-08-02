from pathlib import Path

from core.config import (
    APPLICATION_NAME,
    VERSION,
    DEFAULT_TEMPLATE,
    DEFAULT_PROJECT_LOCATION,
)
from core.template_loader import TemplateLoader
from core.folder_builder import FolderBuilder
from core.document_builder import DocumentBuilder
from core.logger import AtlasLogger
from core.project import Project


class ProjectBuilder:
    """Orchestrates the creation of a new project."""

    def __init__(self):
        self.logger = AtlasLogger()
        self.loader = TemplateLoader()
        self.folder_builder = FolderBuilder()
        self.document_builder = DocumentBuilder()

        self.project_name = ""
        self.project_path = None
        self.template_name = DEFAULT_TEMPLATE

    def run(self):
        self.logger.header(f"{APPLICATION_NAME} v{VERSION}")
        self.logger.info(f"Company: Vector Labs | Author: Ashe Von\n")

        self.get_project_name()
        self.create_project()

    def get_project_name(self):
        while True:
            name = input("Project Name: ").strip()

            if not name:
                self.logger.info("Project name cannot be empty. Please try again.\n")
                continue

            # Very basic sanitization (you can improve this later)
            if any(char in name for char in r'<>:"/\|?*'):
                self.logger.info("Project name contains invalid characters. Please try again.\n")
                continue

            self.project_name = name
            break

    def create_project(self):
        self.project_path = DEFAULT_PROJECT_LOCATION / self.project_name

        if self.project_path.exists():
            self.logger.info(f"\nA project already exists at:\n{self.project_path}")
            self.logger.info("Please choose a different name or delete the existing folder.\n")
            return

        # Create the root project folder
        self.project_path.mkdir(parents=True, exist_ok=True)

        # Load template
        try:
            template = self.loader.load(self.template_name)
        except FileNotFoundError as e:
            self.logger.info(str(e))
            return

        # Create folders
        self.folder_builder.create(self.project_path, template)

        # Create documentation
        self.logger.section("Generating Documentation")
        self.document_builder.create(self.project_path, self.project_name)

        # Final summary
        self.logger.header("Project created successfully!")
        self.logger.info(f"Name:     {self.project_name}")
        self.logger.info(f"Location: {self.project_path}")
        self.logger.info(f"Template: {self.template_name}")
        self.logger.info("\nYou can now open this folder in Unreal Engine or your preferred tools.")