# Update Device Status

from search import search_device


def update_device_status(device_name, new_status):
    """
    Update the status of an existing device.
    Returns True if the update is successful.
    Returns False if the device is not found
    or the status is invalid.
    """

    device = search_device(device_name)

    if device is None:
        return False

    valid_statuses = [
        "Online",
        "Offline",
        "Under Maintenance"
    ]

    if new_status not in valid_statuses:
        return False

    device["status"] = new_status

    return True
