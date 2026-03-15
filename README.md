# Unit Converter

A small Python unit converter project with functions for temperature, distance, and weight conversions. The repo includes automated tests with both `pytest` and `unittest`, plus GitHub Actions workflows that run on pushes to `main`.

## Project Structure

```text
unit-converter/
|-- .github/
|   `-- workflows/
|       |-- pytest_action.yml
|       `-- unittest_action.yml
|-- data/
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

## Available Conversions

| Category | Function | Description |
|---|---|---|
| Temperature | `celsius_to_fahrenheit()` | Celsius to Fahrenheit |
| Temperature | `fahrenheit_to_celsius()` | Fahrenheit to Celsius |
| Temperature | `celsius_to_kelvin()` | Celsius to Kelvin |
| Distance | `miles_to_kilometers()` | Miles to kilometers |
| Distance | `kilometers_to_miles()` | Kilometers to miles |
| Weight | `pounds_to_kilograms()` | Pounds to kilograms |
| Weight | `kilograms_to_pounds()` | Kilograms to pounds |

## Validation Rules

- Temperature inputs must be numeric.
- `celsius_to_kelvin()` rejects values below absolute zero (`-273.15` C).
- Distance and weight inputs must be numeric and non-negative.

## Installation

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

## CI/CD

The repo includes two GitHub Actions workflows in `.github/workflows/`:

- `pytest_action.yml`: runs the `pytest` suite on pushes to `main`
- `unittest_action.yml`: runs the `unittest` suite on pushes to `main`

## Main Files

- [`src/converter.py`](./src/converter.py): conversion logic and input validation
- [`test/test_pytest.py`](./test/test_pytest.py): test coverage using `pytest`
- [`test/test_unittest.py`](./test/test_unittest.py): test coverage using `unittest`
