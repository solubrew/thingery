# Thingery Skill

## Description
Thingery is a physical/chemical data library providing element properties, material data, food nutrition information, scientific scales, and protocols.

## Capabilities
- Access periodic table elements with full properties
- Query material properties (density, melting point, etc.)
- Search food nutritional data
- Get scientific scale information
- Access physical constants

## Usage

### CLI
```bash
thingery list-elements
thingery list-materials
thingery search <query>
thingery element <symbol>
thingery scale <name>
```

### Python
```python
from thingery.elements import ELEMENTS
from thingery.materials import MATERIALS

h = ELEMENTS["H"]
print(h.name, h.atomic_mass)
```

## Files
- `thingery/__init__.py` - Package entry
- `thingery/cli.py` - CLI interface
- `thingery/elements/` - Element data
- `thingery/materials/` - Material data
- `thingery/food/` - Food data
- `thingery/scales.py` - Scale definitions
- `thingery/protocols.py` - Protocols
- `thingery/colors.py` - Color definitions
- `thingery/constants.py` - Physical constants

## Dependencies
- click (CLI)
- yaml (data loading)
