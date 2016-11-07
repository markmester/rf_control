import yaml

with open('config/config.yaml', 'r+') as f:
    config = yaml.load(f)


def get_device(device):
    devices = config['devices']

    # logic to determine which device has been requested
    if 'light' in device:
        device = [x for x in devices if x['device'] == 'lights'][0]

    return device
