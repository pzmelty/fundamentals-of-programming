# tv_show.py file

from tv import TV


def main():

    # Create TV set
    my_tv = TV()

    # Set TV channels
    my_tv.set_channels([
        "TVP1",
        "TVP2",
        "Polsat",
        "TVN",
        "Filmbox",
        "Discovery",
        "HBO"
    ])

    # Turn TV on
    my_tv.turn_on()

    # Show TV status
    my_tv.show_status()

    # Increase volume
    my_tv.increase_volume()
    my_tv.increase_volume()
    my_tv.increase_volume()

    # Show TV status
    my_tv.show_status()

    # Decrease volume
    my_tv.decrease_volume()

    # Show TV status
    my_tv.show_status()

    # Try to increase volume above 10
    for i in range(12):
        my_tv.increase_volume()

    my_tv.show_status()

    # Try to decrease volume below 0
    for i in range(12):
        my_tv.decrease_volume()

    my_tv.show_status()


if __name__ == "__main__":
    main()
