from pathlib import Path


class FolderBuilder:

    def create(self, project_path, template):

        folders = template["folders"]

        print("\nCreating Folder Structure\n")

        for folder in folders:

            current = project_path / Path(folder)

            current.mkdir(
                parents=True,
                exist_ok=True
            )

            print(f"✓ {folder}")

        print("\nFolder creation complete.")