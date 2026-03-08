# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Materials Module
	description: >
		Material data models and implementations
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# ======================================Standard Library Modules======================================================||
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
from thingery.models import Material, MaterialCategory, MaterialProperty

# ====================================================================================================================||

# Common Metals
IRON = Material(
	name="Iron",
	formula="Fe",
	category=MaterialCategory.METAL.value,
	density=7874,
	melting_point=1811,
	boiling_point=3134,
	description="Iron is a metal in the first transition series.",
	electrical_conductivity=1.0e7,
	thermal_conductivity=80.4,
)

COPPER_METAL = Material(
	name="Copper",
	formula="Cu",
	category=MaterialCategory.METAL.value,
	density=8960,
	melting_point=1357.77,
	boiling_point=2835,
	description="Copper is a soft, malleable, and ductile metal.",
	electrical_conductivity=5.96e7,
	thermal_conductivity=401,
)

ALUMINUM = Material(
	name="Aluminum",
	formula="Al",
	category=MaterialCategory.METAL.value,
	density=2698,
	melting_point=933.47,
	boiling_point=2792,
	description="Aluminum is a silvery-white, soft, non-magnetic and ductile metal.",
	electrical_conductivity=3.77e7,
	thermal_conductivity=237,
)

GOLD_METAL = Material(
	name="Gold",
	formula="Au",
	category=MaterialCategory.METAL.value,
	density=19300,
	melting_point=1337.33,
	boiling_point=3129,
	description="Gold is a bright, slightly reddish yellow, dense, soft, malleable, and ductile metal.",
	electrical_conductivity=4.1e7,
	thermal_conductivity=317,
)

SILVER_METAL = Material(
	name="Silver",
	formula="Ag",
	category=MaterialCategory.METAL.value,
	density=10500,
	melting_point=1234.93,
	boiling_point=2435,
	description="Silver is a soft, white, lustrous transition metal.",
	electrical_conductivity=6.3e7,
	thermal_conductivity=429,
)

TITANIUM = Material(
	name="Titanium",
	formula="Ti",
	category=MaterialCategory.METAL.value,
	density=4506,
	melting_point=1941,
	boiling_point=3560,
	description="Titanium is a lustrous transition metal with high strength and low density.",
	electrical_conductivity=2.38e6,
	thermal_conductivity=21.9,
)

# Alloys
STEEL = Material(
	name="Steel",
	formula="Fe+C",
	category=MaterialCategory.ALLOY.value,
	density=7850,
	melting_point=1800,
	boiling_point=3133,
	description="Steel is an alloy of iron and carbon.",
	electrical_conductivity=6.99e6,
	thermal_conductivity=50.2,
	tensile_strength=400,
	youngs_modulus=200,
)

STAINLESS_STEEL = Material(
	name="Stainless Steel",
	formula="Fe+Cr+Ni",
	category=MaterialCategory.ALLOY.value,
	density=8000,
	melting_point=1700,
	boiling_point=3000,
	description="Stainless steel is a corrosion-resistant steel alloy.",
	electrical_conductivity=1.4e6,
	thermal_conductivity=16.3,
	tensile_strength=505,
	youngs_modulus=193,
)

BRASS = Material(
	name="Brass",
	formula="Cu+Zn",
	category=MaterialCategory.ALLOY.value,
	density=8500,
	melting_point=1200,
	boiling_point=1800,
	description="Brass is an alloy of copper and zinc.",
	electrical_conductivity=1.6e7,
	thermal_conductivity=150,
	tensile_strength=300,
	youngs_modulus=100,
)

BRONZE = Material(
	name="Bronze",
	formula="Cu+Sn",
	category=MaterialCategory.ALLOY.value,
	density=8700,
	melting_point=1200,
	boiling_point=2200,
	description="Bronze is an alloy of copper and tin.",
	electrical_conductivity=1.2e7,
	thermal_conductivity=26,
	tensile_strength=350,
	youngs_modulus=110,
)

# Polymers
POLYETHYLENE = Material(
	name="Polyethylene",
	formula="(C2H4)n",
	category=MaterialCategory.POLYMER.value,
	density=950,
	melting_point=397,
	boiling_point=None,
	description="Polyethylene is the most widely produced plastic.",
	electrical_conductivity=1.0e-16,
	thermal_conductivity=0.33,
	tensile_strength=30,
	youngs_modulus=0.2,
)

POLYPROPYLENE = Material(
	name="Polypropylene",
	formula="(C3H6)n",
	category=MaterialCategory.POLYMER.value,
	density=900,
	melting_point=420,
	boiling_point=None,
	description="Polypropylene is a thermoplastic polymer.",
	electrical_conductivity=1.0e-16,
	thermal_conductivity=0.22,
	tensile_strength=32,
	youngs_modulus=1.5,
)

NYLON = Material(
	name="Nylon",
	formula="(C12H22N2O2)n",
	category=MaterialCategory.POLYMER.value,
	density=1140,
	melting_point=530,
	boiling_point=None,
	description="Nylon is a synthetic polymer.",
	electrical_conductivity=1.0e-12,
	thermal_conductivity=0.25,
	tensile_strength=75,
	youngs_modulus=2.0,
)

# Ceramics
ALUMINA = Material(
	name="Alumina",
	formula="Al2O3",
	category=MaterialCategory.CERAMIC.value,
	density=3980,
	melting_point=2345,
	boiling_point=3250,
	description="Alumina is an aluminum oxide ceramic.",
	electrical_conductivity=1.0e-14,
	thermal_conductivity=30,
	hardness="9 Mohs",
)

SILICON_CARBIDE = Material(
	name="Silicon Carbide",
	formula="SiC",
	category=MaterialCategory.CERAMIC.value,
	density=3210,
	melting_point=3000,
	boiling_point=None,
	description="Silicon carbide is a very hard ceramic.",
	electrical_conductivity=1.0e3,
	thermal_conductivity=120,
	hardness="9.5 Mohs",
)

# Semiconductors
SILICON = Material(
	name="Silicon",
	formula="Si",
	category=MaterialCategory.SEMICONDUCTOR.value,
	density=2329,
	melting_point=1687,
	boiling_point=3538,
	description="Silicon is a semiconductor material.",
	electrical_conductivity=1.0e-3,
	thermal_conductivity=149,
)

GERMANIUM = Material(
	name="Germanium",
	formula="Ge",
	category=MaterialCategory.SEMICONDUCTOR.value,
	density=5323,
	melting_point=1211.40,
	boiling_point=3106,
	description="Germanium is a semiconductor material.",
	electrical_conductivity=2.2,
	thermal_conductivity=59.9,
)

GALLIUM_ARSENIDE = Material(
	name="Gallium Arsenide",
	formula="GaAs",
	category=MaterialCategory.SEMICONDUCTOR.value,
	density=5317,
	melting_point=1511,
	boiling_point=None,
	description="Gallium arsenide is a compound semiconductor.",
	electrical_conductivity=1.0e-6,
	thermal_conductivity=45,
)

# Composites
CARBON_FIBER = Material(
	name="Carbon Fiber Composite",
	formula="C",
	category=MaterialCategory.COMPOSITE.value,
	density=1600,
	melting_point=3500,
	boiling_point=None,
	description="Carbon fiber reinforced polymer.",
	tensile_strength=4000,
	youngs_modulus=230,
)

# Export all materials
__all__ = [
	'Iron', 'Copper', 'Aluminum', 'Gold', 'Silver', 'Titanium',
	'Steel', 'StainlessSteel', 'Brass', 'Bronze',
	'Polyethylene', 'Polypropylene', 'Nylon',
	'Alumina', 'SiliconCarbide',
	'Silicon', 'Germanium', 
	'Carbon Fiber Composite',
]
