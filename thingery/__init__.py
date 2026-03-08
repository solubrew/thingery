# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery
	description: >
		Thingery - Physical/Chemical Data Library
		Complete database of elements, materials, foods, institutions, colors, scales, and protocols
	version: 0.1.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
from thingery.models import (
	Element, Isotope, Material, Alloy, Polymer, Ceramic,
	Food, Nutrition, Institution, Color, Scale, Protocol,
	ElementCategory, Phase, DecayMode, MaterialCategory, InstitutionType
)

from thingery.elements.elements import (
	Hydrogen, Helium, Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen,
	Fluorine, Neon, Sodium, Magnesium, Aluminum, Silicon, Phosphorus,
	Sulfur, Chlorine, Argon, Potassium, Calcium,
	Iron, Copper, Silver, Gold
)

from thingery.materials.materials import (
	Iron as IronMaterial, Copper as CopperMaterial, Aluminum as AluminumMaterial, 
	Gold as GoldMaterial, Silver as SilverMaterial, Titanium, Magnesium as MagnesiumMaterial,
	Zinc, Nickel, Lead, Steel, StainlessSteel, Brass, Bronze, CastIron,
	Polyethylene, Polypropylene, Polystyrene, PolyvinylChloride, Nylon,
	Alumina, Zirconia, SiliconCarbide, SiliconSemiconductor, Germanium, GalliumArsenide,
	Glass, CarbonFiberComposite, Quartz, Graphite, Water, Ethanol
)

from thingery.food.foods import (
	Apple, Banana, Orange, Strawberry, Blueberry, Grape, Watermelon, Mango,
	Broccoli, Carrot, Spinach, Tomato, Potato, Onion,
	ChickenBreast, Beef, Salmon, Egg, Tofu,
	Rice, Wheat, Oatmeal,
	Milk, Cheese, Yogurt,
	Coffee, Tea, OrangeJuice, OliveOil
)

from thingery.institutions.institutions import (
	MIT, Stanford, Harvard, Caltech, Oxford, Cambridge, ETHZurich, Tsinghua,
	NIST, LosAlamos, OakRidge, Argonne, JPL, CERN,
	SpaceX, Tesla, Google, Microsoft, IBM, Intel, NVIDIA, AppleCompany
)

from thingery.colors import (
	Red, Maroon, Crimson, Coral, Orange, Yellow, Gold,
	Green, Lime, ForestGreen, SeaGreen,
	Blue, Navy, RoyalBlue, SkyBlue, Cyan, Teal,
	Purple, Violet, Indigo,
	Pink, HotPink, Brown, SaddleBrown,
	White, Black, Gray, Silver
)

from thingery.scales import (
	Kelvin, Celsius, Fahrenheit, Rankine,
	Pascal, Atmosphere, Bar, PSI, Torr,
	Meter, Kilometer, Centimeter, Millimeter, Mile, Foot, Inch,
	Kilogram, Gram, Milligram, Pound, Ounce, Ton,
	Ampere, Volt, Ohm, Watt, Coulomb, Farad, Henry,
	Becquerel, Gray as GrayRadiation, Sievert
)

# ====================================================================================================================||


__version__ = "0.1.0"

__all__ = [
	# Models
	'Element', 'Isotope', 'Material', 'Alloy', 'Polymer', 'Ceramic',
	'Food', 'Nutrition', 'Institution', 'Color', 'Scale', 'Protocol',
	'ElementCategory', 'Phase', 'DecayMode', 'MaterialCategory', 'InstitutionType',
	
	# Elements
	'Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen',
	'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus',
	'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium',
	'Iron', 'Copper', 'Silver', 'Gold',
	
	# Materials
	'IronMaterial', 'CopperMaterial', 'AluminumMaterial', 'GoldMaterial', 'SilverMaterial', 
	'Titanium', 'MagnesiumMaterial', 'Zinc', 'Nickel', 'Lead',
	'Steel', 'StainlessSteel', 'Brass', 'Bronze', 'CastIron',
	'Polyethylene', 'Polypropylene', 'Polystyrene', 'PolyvinylChloride', 'Nylon',
	'Alumina', 'Zirconia', 'SiliconCarbide', 'SiliconSemiconductor', 'Germanium', 'GalliumArsenide',
	'Glass', 'CarbonFiberComposite', 'Quartz', 'Graphite', 'Water', 'Ethanol',
	
	# Foods
	'Apple', 'Banana', 'Orange', 'Strawberry', 'Blueberry', 'Grape', 'Watermelon', 'Mango',
	'Broccoli', 'Carrot', 'Spinach', 'Tomato', 'Potato', 'Onion',
	'ChickenBreast', 'Beef', 'Salmon', 'Egg', 'Tofu',
	'Rice', 'Wheat', 'Oatmeal',
	'Milk', 'Cheese', 'Yogurt',
	'Coffee', 'Tea', 'OrangeJuice', 'OliveOil',
	
	# Institutions
	'MIT', 'Stanford', 'Harvard', 'Caltech', 'Oxford', 'Cambridge', 'ETHZurich', 'Tsinghua',
	'NIST', 'LosAlamos', 'OakRidge', 'Argonne', 'JPL', 'CERN',
	'SpaceX', 'Tesla', 'Google', 'Microsoft', 'IBM', 'Intel', 'NVIDIA', 'AppleCompany',
	
	# Colors
	'Red', 'Maroon', 'Crimson', 'Coral', 'Orange', 'Yellow', 'Gold',
	'Green', 'Lime', 'ForestGreen', 'SeaGreen',
	'Blue', 'Navy', 'RoyalBlue', 'SkyBlue', 'Cyan', 'Teal',
	'Purple', 'Violet', 'Indigo',
	'Pink', 'HotPink', 'Brown', 'SaddleBrown',
	'White', 'Black', 'Gray', 'Silver',
	
	# Scales
	'Kelvin', 'Celsius', 'Fahrenheit', 'Rankine',
	'Pascal', 'Atmosphere', 'Bar', 'PSI', 'Torr',
	'Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Mile', 'Foot', 'Inch',
	'Kilogram', 'Gram', 'Milligram', 'Pound', 'Ounce', 'Ton',
	'Ampere', 'Volt', 'Ohm', 'Watt', 'Coulomb', 'Farad', 'Henry',
	'Becquerel', 'GrayRadiation', 'Sievert',
]
