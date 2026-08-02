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


class ProjectBuilder:

    def __init__(self):

        self.project_name = ""

        self.project_path = None

        self.template = DEFAULT_TEMPLATE

        self.loader = TemplateLoader()

        self.folder_builder = FolderBuilder()

        self.document_builder = DocumentBuilder()

    def run(self):

        print("=" * 40)
        print(APPLICATION_NAME)
        print(VERSION)
        print("=" * 40)

        self.get_project_name()

        self.create_project()

    def get_project_name(self):

        self.project_name = input(
            "Project Name: "
        )

    def create_project(self):

        self.project_path = (
            DEFAULT_PROJECT_LOCATION
            / self.project_name
        )

        self.project_path.mkdir(
            parents=True,
            exist_ok=True
        )

        template = self.loader.load(
            self.template
        )

        self.folder_builder.create(

            self.project_path,

            template["folders"]

        )

        self.document_builder.create(

            self.project_path,

            self.project_name

        )

        print()

        print("=" * 40)

        print("Project created successfully!")

        print(self.project_path)

        print("=" * 40)