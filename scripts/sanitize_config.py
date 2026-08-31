import yaml

SENSITIVE_KEYS = {"password", "token", "secret", "api_key"}

with open("configs/prod/payment-service.yaml", "r") as f:
    config = yaml.safe_load(f)

def sanitize(data):
    if isinstance(data, dict):
        cleaned = {}
        for key, value in data.items():
            if key.lower() in SENSITIVE_KEYS:
                cleaned[key] = "***REDACTED***"
            else:
                cleaned[key] = sanitize(value)
        return cleaned
    elif isinstance(data, list):
        return [sanitize(item) for item in data]
    else:
        return data

sanitized = sanitize(config)

with open("configs/prod/payment-service-sanitized.yaml", "w") as f:
    yaml.safe_dump(sanitized, f, sort_keys=False)

print("Sanitized config created.")
