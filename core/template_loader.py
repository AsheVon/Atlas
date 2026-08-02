import json
from pathlib import Path


class TemplateLoader:

    def __init__(self):

        self.template_data = None


    def load(self, template_name):

        template_file = (
            Path("templates")
            / f"{template_name}.json"
        )

        with open(template_file, "r") as file:

            self.template_data = json.load(file)

        return self.template_data