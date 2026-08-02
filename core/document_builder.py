from core.config import (
    VERSION,
    COMPANY,
    APPLICATION_NAME
)


class DocumentBuilder:

    def create(self, project_path, project_name):

        self.create_readme(project_path, project_name)

        self.create_changelog(project_path)

        self.create_todo(project_path)

        self.create_license(project_path)

        self.create_version(project_path)


    def create_readme(self, project_path, project_name):

        (project_path / "README.md").write_text(
f"""# {project_name}

Created with {APPLICATION_NAME}

Company: {COMPANY}

Version: {VERSION}

Status: In Development
"""
        )

        print("✓ README.md")


    def create_changelog(self, project_path):

        (project_path / "CHANGELOG.md").write_text(
f"""# CHANGELOG

## {VERSION}

Initial Project Created
"""
        )

        print("✓ CHANGELOG.md")


    def create_todo(self, project_path):

        (project_path / "TODO.md").write_text(
"""# TODO

- Begin Project
- Setup Assets
- Import into Unreal
"""
        )

        print("✓ TODO.md")


    def create_license(self, project_path):

        (project_path / "LICENSE.txt").write_text(
f"""{APPLICATION_NAME}

Copyright (c) {COMPANY}

Internal Use
"""
        )

        print("✓ LICENSE.txt")


    def create_version(self, project_path):

        (project_path / "VERSION.txt").write_text(
VERSION
        )

        print("✓ VERSION.txt")