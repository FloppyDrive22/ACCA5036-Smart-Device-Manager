# Display Devices

from devices import devices


def display_devices():
    """
    Display all registered smart devices with
    their room and current status.
    """

    print("\n========== Bright Minds Smart Home Hub ==========\n")

    for device in devices:
        print(f"Device : {device['name']}")
        print(f"Room   : {device['room']}")
        print(f"Status : {device['status']}")
        print("-" * 30)