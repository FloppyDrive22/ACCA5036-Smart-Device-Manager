ffrom devices import devices


def search_device(device_name):
    """
    Search for a device by its name.
    Returns the device dictionary if found.
    Returns None if the device does not exist.
    """

    device_name = device_name.strip().lower()

    for device in devices:
        if device["name"].lower() == device_name:
            return device

    return None
