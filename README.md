# Unit Converter

A Python unit converter module with functions for **Temperature**, **Distance**, and **Weight** conversions. Includes full test coverage using both `pytest` and `unittest`, with GitHub Actions CI/CD workflows.

---

## Project Structure

```
unit-converter/
├── data/
├── src/
│   ├── __init__.py
│   └── converter.py
├── test/
│   ├── __init__.py
│   ├── test_pytest.py
│   └── test_unittest.py
├── workflows/
│   ├── lab1_pytest_action.yml
│   └── lab2_unittest_action.yml
├── requirements.txt
└── README.md
```

---

## Available Conversions

| Category    | Function                  | Description              |
|-------------|---------------------------|--------------------------|
| Temperature | `celsius_to_fahrenheit()` | Celsius → Fahrenheit     |
| Temperature | `fahrenheit_to_celsius()` | Fahrenheit → Celsius     |
| Temperature | `celsius_to_kelvin()`     | Celsius → Kelvin         |
| Distance    | `miles_to_kilometers()`   | Miles → Kilometers       |
| Distance    | `kilometers_to_miles()`   | Kilometers → Miles       |
| Weight      | `pounds_to_kilograms()`   | Pounds → Kilograms       |
| Weight      | `kilograms_to_pounds()`   | Kilograms → Pounds       |

---

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

**Pytest:**
```bash
pytest
```

**Unittest:**
```bash
python -m unittest test.test_unittest
```

---

## CI/CD

Two GitHub Actions workflows are included in the `workflows/` folder:
- **lab1_pytest_action.yml** — Runs pytest on push to `main`
- **lab2_unittest_action.yml** — Runs unittest on push to `main`
