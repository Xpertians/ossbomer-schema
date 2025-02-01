import json
import os
from jsonschema import validate as json_validate
from xmlschema import validate as xml_validate

class SBOMSchemaValidator:
    def __init__(self):
        self.schemas = {}
        schemas_dir = os.path.join(os.path.dirname(__file__), "schemas")  # Correct path handling

        for filename in os.listdir(schemas_dir):
            name, ext = os.path.splitext(filename)
            path = os.path.join(schemas_dir, filename)
            if ext == ".json":
                with open(path, "r") as f:
                    try:
                        self.schemas[name] = json.load(f)
                    except json.JSONDecodeError as e:
                        print(f"Error loading JSON schema {filename}: {e}") # Handle schema loading errors
                        raise  # Re-raise to stop initialization
            elif ext == ".xsd" or ext == ".xml":
                self.schemas[name] = path  # Store path for XML Schema


    def validate_spdx_json(self, file_path: str) -> str:
        try:
            with open(file_path, "r") as f:
                sbom_data = json.load(f)
            json_validate(instance=sbom_data, schema=self.schemas["spdx-schema"])  # Correct key
            return "Valid"
        except json.JSONDecodeError as e: # Handle JSON errors
            return f"JSON Error: {e}"
        except Exception as e:
            return str(e)

    def validate_spdx_xml(self, file_path: str) -> str:
        try:
            xml_validate(file_path, self.schemas["spdx-schema"])  # Correct key
            return "Valid"
        except Exception as e:
            return str(e)

    def validate_cyclonedx_json(self, file_path: str) -> str:
        try:
            with open(file_path, "r") as f:
                sbom_data = json.load(f)
            json_validate(instance=sbom_data, schema=self.schemas["bom-1.4.schema"])  # Correct Key
            return "Valid"
        except json.JSONDecodeError as e: # Handle JSON errors
            return f"JSON Error: {e}"
        except Exception as e:
            return str(e)

    def validate_cyclonedx_xml(self, file_path: str) -> str:
        try:
            xml_validate(file_path, self.schemas["bom-1.4"])  # Correct key
            return "Valid"
        except Exception as e:
            return str(e)