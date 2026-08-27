import json
import yaml
from pathlib import Path
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from yaml import YAMLError

base_dir = Path(__file__).resolve().parent.parent

config_file = base_dir / "configs" / "payment-service.yaml"
schema_file = base_dir / "schemas" / "payment-service-schema.json"

try:
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    print("YAML syntax validation: PASSED")

except YAMLError as error:
    print("YAML syntax validation: FAILED")
    print(error)
    raise SystemExit(1)

with open(schema_file, "r") as file:
    schema = json.load(file)

try:
    validate(instance=config, schema=schema)

    print("JSON Schema validation: PASSED")
    print("Configuration is valid.")

except ValidationError as error:
    print("JSON Schema validation: FAILED")
    print(f"Error: {error.message}")
    raise SystemExit(1)