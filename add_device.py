# Add Device

from devices import devices


def add_device(name, room, status):
    """
    Add a new smart device to the device list.
    Returns True if the device is added successfully.
    Returns False if the entered status is invalid.
    """

    valid_statuses = [
        "Online",
        "Offline",
        "Under Maintenance"
    ]

    if status not in valid_statuses:
        return False

    new_device = {
        "name": name,
        "room": room,
        "status": status
    }

    devices.append(new_device)

    return True