# Thingery

Physical and Chemical Data Library - A comprehensive library of elements, materials, food nutrition, scales, protocols, colors, and constants.

## Overview

Thingery provides structured data for:

- **Elements** - Periodic table with full properties
- **Materials** - Material properties (density, melting point, etc.)
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
from thingery.elements import ELEMENTS
from thingery.materials import MATERIALS
from thingery.scales import SCALES

# Access elements
h = ELEMENTS["H"]
print(f"Hydrogen: {h.atomic_mass}")

# Access materials
water = materials.MATERIALS.get("Water")

# Access scales
temp_scale = SCALES["temperature"]
```

## Development

```bash
# Install in development mode
pip install -e .

# Run tests
pytest tests/

# Run linter
ruff check thingery/
```

## License

MIT
