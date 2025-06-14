import pathlib
import unittest
import yaml

class TestBuildYaml(unittest.TestCase):
    def test_parse_build_yaml(self):
        build_file = pathlib.Path(__file__).resolve().parents[1] / "build.yaml"
        with open(build_file, 'r') as f:
            data = yaml.safe_load(f)
        self.assertIsNotNone(data)

if __name__ == "__main__":
    unittest.main()
