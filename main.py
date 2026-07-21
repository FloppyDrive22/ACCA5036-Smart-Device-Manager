from display import display_devices
from search import search_device
from update import update_device_status
from add_device import add_device


def pause():
    input("\nPress Enter to continue...")


def main():
    while True:
        print("\n=========================================")
        print("      Bright Minds Smart Home Hub")
        print("=========================================")
        print("1. View all devices")
        print("2. Search for a device")
        print("3. Update device status")
        print("4. Add a new device")
        print("5. Exit")
        print("=========================================")

        choice = input("Select an option (1-5): ")

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
