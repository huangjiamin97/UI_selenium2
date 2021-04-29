import yaml

with open('../Data/action.yaml') as f:
    print(yaml.safe_load(f)[0])