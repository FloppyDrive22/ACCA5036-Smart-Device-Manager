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

        if choice == "1":
            display_devices()
            pause()

        elif choice == "2":
            device_name = input("Enter device name: ")
            device = search_device(device_name)

            if device is None:
                print("Device not found.")
            else:
                print("\n========== Device Information ==========")
                print(f"Name   : {device['name']}")
                print(f"Room   : {device['room']}")
                print(f"Status : {device['status']}")
                print("========================================")

            pause()

        elif choice == "3":
            device_name = input("Enter device name: ")
            new_status = input("Enter new status (Online, Offline, Under Maintenance): ")

            updated = update_device_status(device_name, new_status)

            if updated:
                print("Device status updated successfully.")
            else:
                print("Device not found or invalid status.")

            pause()

        elif choice == "4":
            name = input("Enter new device name: ")
            room = input("Enter room: ")
            status = input("Enter status (Online, Offline, Under Maintenance): ")

            added = add_device(name, room, status)

            if added:
                print("Device added successfully.")
            else:
                print("Invalid status. Device was not added.")

            pause()

        elif choice == "5":
            print("Exiting Bright Minds Smart Home Hub.")
            break

        else:
            print("Invalid option. Please select a number from 1 to 5.")
            pause()


if __name__ == "__main__":
    main()
