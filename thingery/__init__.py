"""Thingery - Physical/Chemical Data Library"""

__version__ = "0.1.0"

# Models
from thingery.models import (
	Element, Isotope, ElectronConfiguration,
	Material, Alloy, Composite,
	Food, NutritionInfo,
	Institution,
	Color,
	Scale, Unit,
	Protocol, ProtocolStep,
	ElementCategory, Phase, DecayMode,
	MaterialCategory, InstitutionType, FoodCategory,
)

# Elements
from thingery.elements.hydrogen import Hydrogen
from thingery.elements.helium import Helium
from thingery.elements.nitrogen import Nitrogen
from thingery.elements.oxygen import Oxygen
from thingery.elements.carbon import Carbon
from thingery.elements.copper import Copper
from thingery.elements.gold import Gold
from thingery.elements.silver import Silver

# Materials
from thingery.materials.materials import (
	Iron, Copper, Aluminum, Gold, Silver, Titanium,
	# Steel, Stainless Steel, Brass, Bronze,
	Steel, StainlessSteel, Brass, Bronze,
	Polyethylene, Polypropylene, Nylon,
	Alumina, Silicon Carbide,
	Silicon, Germanium, Gallium Arsenide,
	Carbon Fiber Composite,
)

# Food
from thingery.food.foods import (
	Apple, Banana, Orange, Milk, Beef, Pork,
	Chicken, Eggs, Rice, Wheat, Bread, Sugar,
	Almonds, Orange Juice,
)

# Colors
from thingery.colors import *

# Scales
from thingery.scales import *

# Protocols
from thingery.protocols import *

__all__ = [
    # Version
    "__version__",
    # Models
    "Element", "Isotope", "ElectronConfiguration",
    "Material", "Alloy", "Composite",
    "Food", "NutritionInfo",
    "Institution",
    "Color",
    "Scale", "Unit",
    "Protocol", "ProtocolStep",
    "ElementCategory", "Phase", "DecayMode",
    "MaterialCategory", "InstitutionType", "FoodCategory",
    # Elements
    "Hydrogen", "Helium", "Nitrogen", "Oxygen", "Carbon",
    "Copper", "Gold", "Silver",
    # Materials
    "Iron", "Copper", "Aluminum", "Gold", "Silver", "Titanium",
    "Steel", "Stainless Steel", "Brass", "Bronze",
    "Polyethylene", "Polypropylene", "Nylon",
    "Alumina", "Silicon Carbide",
    "Silicon", "Germanium", "Gallium Arsenide",
    "Carbon Fiber Composite",
    # Food
    "Apple", "Banana", "Orange", "Milk", "Beef", "Pork",
    "Chicken", "Eggs", "Rice", "Wheat", "Bread", "Sugar",
    "Almonds", "Orange Juice",
    # Other exports
    "elements", "materials", "scales", "protocols", "colors", "constants",
]
