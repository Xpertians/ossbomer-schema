import json
import xmlschema
import requests
from jsonschema import validate, ValidationError

# SPDX and CycloneDX schema URLs
SCHEMAS = {
    "spdx": {
        "json": "https://raw.githubusercontent.com/spdx/spdx-spec/v2.3/schemas/spdx-schema.json",
        "xml": "https://raw.githubusercontent.com/spdx/spdx-spec/v2.3/schemas/spdx-schema.xml"
    },
    "cyclonedx": {
        "json": "https://cyclonedx.org/schema/bom-1.4.schema.json",
        "xml": "https://cyclonedx.org/schema/bom-1.4.xsd"
    }
}

class SBOMSchemaValidator:
    """Validates SBOM files against SPDX and CycloneDX schemas."""

    def __init__(self):
        self.schemas = {}

    def load_schema(self, format_type: str, sbom_type: str):
        """Downloads and caches the schema."""
        if sbom_type not in SCHEMAS or format_type not in SCHEMAS[sbom_type]:
            raise ValueError(f"Unsupported SBOM type '{sbom_type}' or format '{format_type}'")
        
        url = SCHEMAS[sbom_type][format_type]
        if url not in self.schemas:
            response = requests.get(url)
            response.raise_for_status()
            self.schemas[url] = response.text if format_type == "xml" else json.loads(response.text)
        return self.schemas[url]

    def validate_json(self, sbom_path: str, sbom_type: str):
        """Validates an SBOM JSON file against the correct schema."""
        try:
            with open(sbom_path, "r", encoding="utf-8") as file:
                sbom_data = json.load(file)
            schema = self.load_schema("json", sbom_type)
            validate(instance=sbom_data, schema=schema)
            return True, "SBOM JSON is valid."
        except ValidationError as e:
            return False, f"Validation Error: {e.message}"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def validate_xml(self, sbom_path: str, sbom_type: str):
        """Validates an SBOM XML file against the correct schema."""
        try:
            schema_content = self.load_schema("xml", sbom_type)
            schema = xmlschema.XMLSchema(schema_content)
            schema.validate(sbom_path)
            return True, "SBOM XML is valid."
        except xmlschema.XMLSchemaValidationError as e:
            return False, f"Validation Error: {e.message}"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def validate(self, sbom_path: str, sbom_type: str):
        """Determines format and validates the SBOM accordingly."""
        if sbom_path.endswith(".json"):
            return self.validate_json(sbom_path, sbom_type)
        elif sbom_path.endswith(".xml"):
            return self.validate_xml(sbom_path, sbom_type)
        else:
            return False, "Unsupported file format. Use JSON or XML."
