def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    Args:
        celsius (int/float): Temperature in Celsius.
    Returns:
        float: Temperature in Fahrenheit.
    Raises:
        ValueError: If input is not a number.
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")
    return round((celsius * 9/5) + 32, 2)


def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    Args:
        fahrenheit (int/float): Temperature in Fahrenheit.
    Returns:
        float: Temperature in Celsius.
    Raises:
        ValueError: If input is not a number.
    """
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number.")
    return round((fahrenheit - 32) * 5/9, 2)


def celsius_to_kelvin(celsius):
    """
    Converts Celsius to Kelvin.
    Args:
        celsius (int/float): Temperature in Celsius.
    Returns:
        float: Temperature in Kelvin.
    Raises:
        ValueError: If input is not a number or below absolute zero.
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero is not possible.")
    return round(celsius + 273.15, 2)


def miles_to_kilometers(miles):
    """
    Converts miles to kilometers.
    Args:
        miles (int/float): Distance in miles.
    Returns:
        float: Distance in kilometers.
    Raises:
        ValueError: If input is not a number or is negative.
    """
    if not isinstance(miles, (int, float)):
        raise ValueError("Input must be a number.")
    if miles < 0:
        raise ValueError("Distance cannot be negative.")
    return round(miles * 1.60934, 2)


def kilometers_to_miles(kilometers):
    """
    Converts kilometers to miles.
    Args:
        kilometers (int/float): Distance in kilometers.
    Returns:
        float: Distance in miles.
    Raises:
        ValueError: If input is not a number or is negative.
    """
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number.")
    if kilometers < 0:
        raise ValueError("Distance cannot be negative.")
    return round(kilometers / 1.60934, 2)


def pounds_to_kilograms(pounds):
    """
    Converts pounds to kilograms.
    Args:
        pounds (int/float): Weight in pounds.
    Returns:
        float: Weight in kilograms.
    Raises:
        ValueError: If input is not a number or is negative.
    """
    if not isinstance(pounds, (int, float)):
        raise ValueError("Input must be a number.")
    if pounds < 0:
        raise ValueError("Weight cannot be negative.")
    return round(pounds * 0.453592, 2)


def kilograms_to_pounds(kilograms):
    """
    Converts kilograms to pounds.
    Args:
        kilograms (int/float): Weight in kilograms.
    Returns:
        float: Weight in pounds.
    Raises:
        ValueError: If input is not a number or is negative.
    """
    if not isinstance(kilograms, (int, float)):
        raise ValueError("Input must be a number.")
    if kilograms < 0:
        raise ValueError("Weight cannot be negative.")
    return round(kilograms / 0.453592, 2)
