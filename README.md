# LAB 4 - Unit Converter

A small Python project for converting temperature, distance, and weight units. The repository includes conversion logic in `src/converter.py` and automated tests written with both `pytest` and `unittest`.

## Project Structure

```text
unit-converter/
|-- data/
|   `-- __init__.py
|-- src/
|   |-- __init__.py
|   `-- converter.py
|-- test/
|   |-- __init__.py
|   |-- test_pytest.py
|   `-- test_unittest.py
|-- requirements.txt
`-- README.md
```

## Features

The project currently supports these conversions:

- `celsius_to_fahrenheit()`
- `fahrenheit_to_celsius()`
- `celsius_to_kelvin()`
- `miles_to_kilometers()`
- `kilometers_to_miles()`
- `pounds_to_kilograms()`
- `kilograms_to_pounds()`

## Validation Rules

- All inputs must be numeric (`int` or `float`).
- `celsius_to_kelvin()` raises a `ValueError` for temperatures below `-273.15`.
- Distance and weight conversion functions raise a `ValueError` for negative inputs.

## Installation

Install the project dependency with:

```bash
pip install -r requirements.txt
```

## Running Tests

Run the `pytest` suite:

```bash
pytest
```

Run the `unittest` suite:

```bash
python -m unittest test.test_unittest
```

## Main Files

- `src/converter.py`: contains the unit conversion functions and validation checks
- `test/test_pytest.py`: contains test coverage using `pytest`
- `test/test_unittest.py`: contains test coverage using `unittest`

## Screenshots

- test_pytest.py


- test_unittest.py


## Notes

- `requirements.txt` currently includes `pytest`.
- The `data/` folder is present in the repo structure but is not used by the converter logic right now.
