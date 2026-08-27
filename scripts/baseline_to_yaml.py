import yaml
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent

input_file = base_dir / "baseline" / "payment-service.conf"
output_file = base_dir / "configs" / "payment-service.yaml"

raw_config = {}

with open(input_file, "r") as file:
    for line in file:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        key, value = line.split("=", 1)
        raw_config[key.strip()] = value.strip()

config = {
    "application": {
        "name": raw_config["application_name"],
        "environment": raw_config["environment"],
    },
    "server": {
        "port": int(raw_config["server_port"]),
        "ssl_enabled": raw_config["ssl_enabled"].lower() == "true",
    },
    "logging": {
        "level": raw_config["log_level"],
    },
    "database": {
        "host": raw_config["database_host"],
        "port": int(raw_config["database_port"]),
    },
    "performance": {
        "max_connections": int(raw_config["max_connections"]),
    },
}

with open(output_file, "w") as file:
    yaml.safe_dump(config, file, sort_keys=False)

print(f"YAML created successfully: {output_file}")