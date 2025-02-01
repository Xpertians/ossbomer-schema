
# ossbomer-schema

SBOM Schema Validation for SPDX and CycloneDX 📜✅

ossbomer-schema is a Python library that validates Software Bill of Materials (SBOMs) against SPDX and CycloneDX schemas. It ensures SBOMs are properly formatted in JSON and XML before further analysis.

## Features

* Supports SPDX 3.0, SPDX 2.3, and CycloneDX 1.3–1.6
* Validates both JSON and XML formats
* Uses local schemas (no remote dependency issues)
* Outputs results in both human-readable and JSON formats for API integration

## Usage

You can also use ossbomer-schema as a Python library:

from ossbomer_schema.validator import SBOMSchemaValidator

validator = SBOMSchemaValidator()

### Validate SPDX JSON
result = validator.validate_spdx_json("test_sbom.spdx.json")
print(result)  # "Valid" or error message

### Validate CycloneDX XML
result = validator.validate_cyclonedx_xml("test_sbom.cdx.xml")
print(result)  # "Valid" or error message

📂 SBOM Schema Support

| SBOM Format | Version | JSON | XML |
| ----------- | ------- | ---- | --- |
|    SPDX     | 2.3 - 3.0 | ✅   | 🚫 (No official schema) |
|    SPDX     | 2.3     | ✅   | 🚫 (No official schema) |


3.0

✅

🚫 (No official schema)

SPDX

2.3

✅

✅

CycloneDX

1.6

✅

✅

CycloneDX

1.5

✅

✅

CycloneDX

1.4

✅

✅

CycloneDX

1.3

✅

✅

🚨 Note: SPDX 3.0 does not have an official XML schema, so XML validation is unavailable for that version.

📌 How It Works

Loads pre-downloaded schema files from schemas/

Uses jsonschema to validate JSON SBOMs

Uses xmlschema to validate CycloneDX XML SBOMs

Returns detailed validation errors if an SBOM is malformed

📂 Schema Files

Schemas are stored in schemas/ to avoid remote dependency issues.

Format

Version

Schema File

SPDX

3.0

schemas/spdx-schema.json

SPDX

2.3

schemas/spdx-2.3-schema.xsd

CycloneDX

1.6

schemas/bom-1.6.schema.json, schemas/bom-1.6.xsd

CycloneDX

1.5

schemas/bom-1.5.schema.json, schemas/bom-1.5.xsd

CycloneDX

1.4

schemas/bom-1.4.schema.json, schemas/bom-1.4.xsd

CycloneDX

1.3

schemas/bom-1.3.schema.json, schemas/bom-1.3.xsd

✅ Testing

Run the test suite with:

python3 -m unittest discover tests

Sample SBOM test files are in tests/:

test_sbom.spdx.json

test_sbom.spdx.xml

test_sbom.cdx.json

test_sbom.cdx.xml

📜 License

This project is licensed under MIT.

📌 Future Improvements

Add official SPDX 3.0 XML validation (when available).

Extend schema validation for new CycloneDX versions.

Integrate with ossbomer-conformance for regulatory compliance checks.

📫 Questions?

Feel free to open an issue or contribute to the project! 🚀

Does this updated README match your expectations? Let me know if you'd like any refinements before moving on to ossbomer-conformance! 😊