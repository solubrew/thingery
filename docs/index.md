# Thingery Documentation

## Overview

Thingery is a comprehensive physical and chemical data library providing:

- **Elements** - Periodic table data
- **Materials** - Material properties
- **Food** - Nutritional data
- **Scales** - Scientific scales and measurements
- **Protocols** - Standard protocols
- **Colors** - Color definitions
- **Constants** - Physical constants

## Installation

```bash
pip install thingery
```

## CLI Usage

```bash
# List all elements
thingery list-elements

# List all materials
thingery list-materials

# Search for something
thingery search carbon

# Get element info
thingery element H

# Get scale info
thingery scale temperature
```

## Python Usage

```python
from thingery import elements, materials, scales

# Access elements
h = elements.ELEMENTS["H"]
print(f"Hydrogen: {h.atomic_mass}")

# Access materials
water = materials.MATERIALS.get("Water")
```

## Testing

```bash
pytest tests/
```
