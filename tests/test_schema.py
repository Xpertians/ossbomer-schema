from ossbomer_schema.schema import SBOMSchemaValidator

# Test SPDX JSON validation
def test_spdx_json():
    validator = SBOMSchemaValidator()
    result, message = validator.validate("test_sbom.spdx.json", "spdx")
    print("SPDX JSON:", message)

# Test CycloneDX XML validation
def test_cyclonedx_xml():
    validator = SBOMSchemaValidator()
    result, message = validator.validate("test_sbom.cdx.xml", "cyclonedx")
    print("CycloneDX XML:", message)

if __name__ == "__main__":
    test_spdx_json()
    test_cyclonedx_xml()
