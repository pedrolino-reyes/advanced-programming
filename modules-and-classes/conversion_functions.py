"""
This module contains the CLI conversion functions app, which presents the
user with a menu of different conversion options and then converts their
input accordingly.
"""

from weights_and_measures import (
    feet_and_inches_to_metres,
    metres_to_feet_and_inches,
    pounds_to_kilograms,
    kilograms_to_pounds,
    kelvin_to_celsius,
    celsius_to_kelvin,
    hours_and_minutes_to_seconds,
    seconds_to_hours_and_minutes
)


def display_main_menu() -> None:
    """
    Presents the user with a menu of different conversion options.
    """
    print("\nChoose a conversion option:")
    print()
    print("Distance:")
    print("\t1. Feet and inches to metres")
    print("\t2. Metres to feet and inches")
    print()
    print("Weight:")
    print("\t3. Pounds to kilograms")
    print("\t4. Kilograms to pounds")
    print()
    print("Temperature:")
    print("\t5. Kelvin to Celsius")
    print("\t6. Celsius to Kelvin")
    print()
    print("Time:")
    print("\t7. Hours and minutes to seconds")
    print("\t8. Seconds to hours and minutes")
    print()
    print("Quit:")
    print("\t9. Quit")


def handle_feet_to_metres() -> None:
    """
    Handles the conversion of feet and inches to metres.
    """
    feet = float(input("Enter the number of feet: "))
    inches = float(input("Enter the number of inches: "))
    metres = feet_and_inches_to_metres(feet, inches)
    print(f"{feet} feet and {inches} inches is equal to {metres} metres.")


def handle_metres_to_feet() -> None:
    """
    Handles the conversion of metres to feet and inches.
    """
    metres = float(input("Enter the number of metres: "))
    feet, inches = metres_to_feet_and_inches(metres)
    print(f"{metres} metres is equal to {feet} feet and {inches} inches.")


def handle_pounds_to_kilograms() -> None:
    """
    Handles the conversion of pounds to kilograms.
    """
    pounds = float(input("Enter the number of pounds: "))
    kilograms = pounds_to_kilograms(pounds)
    print(f"{pounds} pounds is equal to {kilograms} kilograms.")


def handle_kilograms_to_pounds() -> None:
    """
    Handles the conversion of kilograms to pounds.
    """
    kilograms = float(input("Enter the number of kilograms: "))
    pounds = kilograms_to_pounds(kilograms)
    print(f"{kilograms} kilograms is equal to {pounds} pounds.")


def handle_kelvin_to_celsius() -> None:
    """
    Handles the conversion of Kelvin to Celsius.
    """
    kelvin = float(input("Enter the temperature in Kelvin: "))
    celsius = kelvin_to_celsius(kelvin)
    print(f"{kelvin} Kelvin is equal to {celsius} Celsius.")


def handle_celsius_to_kelvin() -> None:
    """
    Handles the conversion of Celsius to Kelvin.
    """
    celsius = float(input("Enter the temperature in Celsius: "))
    kelvin = celsius_to_kelvin(celsius)
    print(f"{celsius} Celsius is equal to {kelvin} Kelvin.")


def handle_hours_and_minutes_to_seconds() -> None:
    """
    Handles the conversion of hours and minutes to seconds.
    """
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = hours_and_minutes_to_seconds(hours, minutes)
    print(f"{hours} hours and {minutes} minutes is equal to {seconds} seconds.")


def handle_seconds_to_hours_and_minutes() -> None:
    """
    Handles the conversion of seconds to hours and minutes.
    """
    seconds = int(input("Enter the number of seconds: "))
    hours, minutes = seconds_to_hours_and_minutes(seconds)
    print(f"{seconds} seconds is equal to {hours} hours and {minutes} minutes.")


def conversion_functions():
    """
    The main function for the conversion functions app.
    """
    while True:
        display_main_menu()
        try:
            option = int(input("\nChoose an option from the menu: "))
        except ValueError:
            print("\nPlease enter a number.")
            continue

        match option:
            case 1:
                handle_feet_to_metres()
            case 2:
                handle_metres_to_feet()
            case 3:
                handle_pounds_to_kilograms()
            case 4:
                handle_kilograms_to_pounds()
            case 5:
                handle_kelvin_to_celsius()
            case 6:
                handle_celsius_to_kelvin()
            case 7:
                handle_hours_and_minutes_to_seconds()
            case 8:
                handle_seconds_to_hours_and_minutes()
            case 9:
                break
            case _:
                print("Invalid option. Please select one of the options from the menu.")
                continue

        pause = input("Press any key to continue...")
        print()


if __name__ == "__main__":
    conversion_functions()