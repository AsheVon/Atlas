import json
from pathlib import Path


class TemplateLoader:
    """Loads JSON project templates from the templates/ folder."""

    def __init__(self):
        # This finds the templates folder no matter where you run the script from
        self.templates_dir = Path(__file__).resolve().parent.parent / "templates"
        self.template_data = None

    def load(self, template_name: str) -> dict:
        template_file = self.templates_dir / f"{template_name}.json"

        if not template_file.exists():
            raise FileNotFoundError(
                f"Template not found: {template_file}\n"
                f"Available templates are in: {self.templates_dir}"
            )

        with open(template_file, "r", encoding="utf-8") as file:
            self.template_data = json.load(file)

        return self.template_data