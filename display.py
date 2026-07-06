# display.py
# Functions for displaying smart devices.

SEPARATOR = "-" * 30


def print_devices(devices):
    """Display all devices in a formatted way."""

    for device in devices:
        print(f"Device Name: {device['name']}")
        print(f"Room: {device['room']}")
        print(f"Status: {device['status']}")
        print(SEPARATOR)









