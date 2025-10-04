# Thoughtful AI Package Sorter

Robotic automation factory package sorting system.

## Quick Start

```bash
# Install dependencies
pip install pytest

# Run tests
pytest test_package_sorter.py -v

# Use the function
python -c "from package_sorter import sort; print(sort(100, 100, 100, 20))"
```

## Function Signature

```python
sort(width: float, height: float, length: float, mass: float) -> str
```

**Parameters:**
- `width`, `height`, `length`: dimensions in centimeters
- `mass`: weight in kilograms

**Returns:** `"STANDARD"`, `"SPECIAL"`, or `"REJECTED"`

## Classification Rules

- **BULKY**: volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
- **HEAVY**: mass ≥ 20 kg
- **STANDARD**: neither bulky nor heavy
- **SPECIAL**: bulky OR heavy (but not both)
- **REJECTED**: bulky AND heavy

## Examples

```python
from package_sorter import sort

sort(10, 10, 10, 5)      # "STANDARD" - normal package
sort(150, 10, 10, 5)     # "SPECIAL"  - bulky by dimension
sort(100, 100, 100, 10)  # "SPECIAL"  - bulky by volume
sort(50, 50, 50, 25)     # "SPECIAL"  - heavy
sort(150, 10, 10, 20)    # "REJECTED" - bulky and heavy
```

## Test Coverage

32 test cases with 100% code coverage:
- Standard packages
- Bulky classification (volume and dimension)
- Heavy classification
- Rejected packages
- Boundary conditions
- Edge cases (float precision, zero values, mixed types)
- Type safety verified with mypy --strict