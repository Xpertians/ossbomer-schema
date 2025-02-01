import unittest
import os
import json # Import json
from ossbomer_schema.validator import SBOMSchemaValidator

class TestSBOMValidation(unittest.TestCase):
    def setUp(self):
        self.validator = SBOMSchemaValidator()
        self.test_dir = os.path.dirname(__file__)

    def test_valid_spdx_json(self):
        file_path = os.path.join(self.test_dir, "test_sbom.spdx.json")
        # Check if the file exists before attempting to open it
        if os.path.exists(file_path):  # Check if the file exists
            result = self.validator.validate_spdx_json(file_path)
            self.assertEqual(result, "Valid")
        else:
            self.fail(f"Test file not found: {file_path}")

    def test_invalid_spdx_json(self): # Example invalid test
        file_path = os.path.join(self.test_dir, "test_sbom_invalid.spdx.json") # Example invalid test
        if os.path.exists(file_path):  # Check if the file exists
            result = self.validator.validate_spdx_json(file_path)
            self.assertNotEqual(result, "Valid") # Check that it's not valid
        else:
            self.fail(f"Test file not found: {file_path}")

    def test_valid_spdx_xml(self):
         file_path = os.path.join(self.test_dir, "test_sbom.spdx.xml")
         if os.path.exists(file_path):  # Check if the file exists
            result = self.validator.validate_spdx_xml(file_path)
            self.assertEqual(result, "Valid")
         else:
            self.fail(f"Test file not found: {file_path}")

    def test_valid_cyclonedx_json(self):
        file_path = os.path.join(self.test_dir, "test_sbom.cyclonedx.1.4.json")
        if os.path.exists(file_path):  # Check if the file exists
            result = self.validator.validate_cyclonedx_json(file_path)
            self.assertEqual(result, "Valid")
        else:
            self.fail(f"Test file not found: {file_path}")

    def test_valid_cyclonedx_xml(self):
        file_path = os.path.join(self.test_dir, "test_sbom.cyclonedx.1.4.xml")
        if os.path.exists(file_path):  # Check if the file exists
            result = self.validator.validate_cyclonedx_xml(file_path)
            self.assertEqual(result, "Valid")
        else:
            self.fail(f"Test file not found: {file_path}")

    # Add more test cases for invalid SBOMs and edge cases

if __name__ == "__main__":
    unittest.main()