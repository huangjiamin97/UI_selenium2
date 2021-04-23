import yaml

with open(r'F:\UI_selenium\Data\action.yaml') as f:
    actions = yaml.safe_load(f)
    print(actions)
    for action in actions:
        if 'by' in action.keys():
            print(action.keys())
            print(action)
            print(action['by'])


