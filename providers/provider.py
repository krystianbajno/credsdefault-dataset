import yaml

def load_yaml_config(yaml_file_: str, field: str) -> dict:
    with open(yaml_file_, 'r') as file:
        config = yaml.safe_load(file)
    return config.get(field, {})