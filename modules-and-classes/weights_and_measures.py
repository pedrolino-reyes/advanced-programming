"""
Weights and Measures module

This module contains classes and functions for converting between different units of
weight, distance, temperature and time.
"""


def feet_and_inches_to_metres(feet: int, inches: int) -> float:
    """
    Converts a length from feet and inches to metres.

    Parameters:
    feet (int): The number of feet.
    inches (int): The number of inches.

    Returns:
    float: The length in metres.
    """
    # Convert feet to inches and add to the total inches
    total_inches = (feet * 12) + inches
    # Convert inches to metres
    metres = total_inches * 0.0254
    return metres


def metres_to_feet_and_inches(metres: int) -> tuple:
    """
    Converts a length from metres to feet and inches.

    Parameters:
    metres (float): The length in metres.

    Returns:
    tuple: A tuple containing the number of feet and inches.
    """
    # Convert metres to inches
    total_inches = metres / 0.0254
    # Calculate the number of feet
    feet = total_inches // 12
    # Calculate the number of inches
    inches = total_inches % 12
    return feet, inches


def pounds_to_kilograms(pounds: float) -> float:
    """
    Converts a weight from pounds to kilograms.

    Parameters:
    pounds (float): The weight in pounds.

    Returns:
    float: The weight in kilograms.
    """
    kilograms = pounds * 0.453592
    return kilograms


def kilograms_to_pounds(kilograms: float) -> float:
    """
    Converts a weight from kilograms to pounds.

    Parameters:
    kilograms (float): The weight in kilograms.

    Returns:
    float: The weight in pounds.
    """
    pounds = kilograms / 0.453592
    return pounds


def kelvin_to_celsius(kelvin: float) -> float:
    """
    Converts a temperature from Kelvin to Celsius.

    Parameters:
    kelvin (float): The temperature in Kelvin.

    Returns:
    float: The temperature in Celsius, to 2 decimal places.
    """
    celsius = round(kelvin - 273.15, 2)
    return celsius


def celsius_to_kelvin(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Kelvin.

    Parameters:
    celsius (float): The temperature in Celsius.

    Returns:
    float: The temperature in Kelvin.
    """
    kelvin = celsius + 273.15
    return kelvin


def hours_and_minutes_to_seconds(hours: int, minutes: int) -> int:
    """
    Converts a time from hours and minutes to seconds.

    Parameters:
    hours (int): The number of hours.
    minutes (int): The number of minutes.

    Returns:
    int: The time in seconds.
    """
    total_minutes = (hours * 60) + minutes
    seconds = total_minutes * 60
    return seconds


def seconds_to_hours_and_minutes(seconds: int) -> tuple:
    """
    Converts a time from seconds to hours and minutes.

    Parameters:
    seconds (int): The time in seconds.

    Returns:
    tuple: A tuple containing the number of hours and minutes.
    """
    total_minutes = seconds // 60
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    return hours, minutes