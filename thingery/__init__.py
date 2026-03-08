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
	Iron, Cobalt, Nickel, Copper, Zinc, Gallium, Germanium, Arsenic, Selenium,
	Bromine, Krypton,
	Rubidium, Strontium, Yttrium, Zirconium, Niobium, Molybdenum,
	Silver, Gold
)

from thingery.materials.materials import (
	Iron as IronMaterial, Copper as CopperMaterial, Aluminum as AluminumMaterial, 
	Gold as GoldMaterial, Silver as SilverMaterial, Titanium as TitaniumMaterial, 
	Magnesium as MagnesiumMaterial, Zinc, Nickel, Lead, Steel, StainlessSteel, 
	Brass, Bronze, CastIron,
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
	Red, Maroon, Crimson, Coral, Tomato as TomatoColor, FireBrick,
	Orange, DarkOrange, Yellow, Gold, LemonChiffon,
	Green, Lime, ForestGreen, SeaGreen, Olive, DarkGreen, LawnGreen,
	Blue, Navy, RoyalBlue, SkyBlue, Cyan, Teal, DodgerBlue, SteelBlue,
	Purple, Violet, Indigo, Magenta, Pink, HotPink, DeepPink, Lavender,
	Brown, SaddleBrown, Sienna, Chocolate, Peru,
	White, Black, Gray, Silver, LightGray, DarkGray,
	SkyBlueNatural, ForestGreenNatural, OceanBlue, Sand, EarthBrown,
	LeafGreen, SunsetOrange, RosePink, LavenderNatural, MintGreen,
	CadmiumYellow, CadmiumRed, CobaltBlue, TitaniumWhite, IvoryBlack,
	Viridian, RawUmber, BurntSienna, Ultramarine, PhthaloBlue
)

from thingery.scales import (
	Kelvin, Celsius, Fahrenheit, Rankine,
	Pascal, Atmosphere, Bar, PSI, Torr,
	Meter, Kilometer, Centimeter, Millimeter, Mile, Foot, Inch, Yard,
	Kilogram, Gram, Milligram, Pound, Ounce, Ton,
	Ampere, Volt, Ohm, Watt, Coulomb, Farad, Henry, Siemens, Tesla,
	Becquerel, GrayRadiation, Sievert,
	Second, Minute, Hour, Day,
	Joule, Calorie, ElectronVolt, BTU,
	Hertz, Kilohertz, Megahertz,
	Byte, Kilobyte, Megabyte
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
	'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium',
	'Bromine', 'Krypton',
	'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum',
	'Silver', 'Gold',
	
	# Materials
	'IronMaterial', 'CopperMaterial', 'AluminumMaterial', 'GoldMaterial', 'SilverMaterial', 
	'TitaniumMaterial', 'MagnesiumMaterial', 'Zinc', 'Nickel', 'Lead',
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
	'Red', 'Maroon', 'Crimson', 'Coral', 'TomatoColor', 'FireBrick',
	'Orange', 'DarkOrange', 'Yellow', 'Gold', 'LemonChiffon',
	'Green', 'Lime', 'ForestGreen', 'SeaGreen', 'Olive', 'DarkGreen', 'LawnGreen',
	'Blue', 'Navy', 'RoyalBlue', 'SkyBlue', 'Cyan', 'Teal', 'DodgerBlue', 'SteelBlue',
	'Purple', 'Violet', 'Indigo', 'Magenta', 'Pink', 'HotPink', 'DeepPink', 'Lavender',
	'Brown', 'SaddleBrown', 'Sienna', 'Chocolate', 'Peru',
	'White', 'Black', 'Gray', 'Silver', 'LightGray', 'DarkGray',
	'SkyBlueNatural', 'ForestGreenNatural', 'OceanBlue', 'Sand', 'EarthBrown',
	'LeafGreen', 'SunsetOrange', 'RosePink', 'LavenderNatural', 'MintGreen',
	'CadmiumYellow', 'CadmiumRed', 'CobaltBlue', 'TitaniumWhite', 'IvoryBlack',
	'Viridian', 'RawUmber', 'BurntSienna', 'Ultramarine', 'PhthaloBlue',
	
	# Scales
	'Kelvin', 'Celsius', 'Fahrenheit', 'Rankine',
	'Pascal', 'Atmosphere', 'Bar', 'PSI', 'Torr',
	'Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Mile', 'Foot', 'Inch', 'Yard',
	'Kilogram', 'Gram', 'Milligram', 'Pound', 'Ounce', 'Ton',
	'Ampere', 'Volt', 'Ohm', 'Watt', 'Coulomb', 'Farad', 'Henry', 'Siemens', 'Tesla',
	'Becquerel', 'GrayRadiation', 'Sievert',
	'Second', 'Minute', 'Hour', 'Day',
	'Joule', 'Calorie', 'ElectronVolt', 'BTU',
	'Hertz', 'Kilohertz', 'Megahertz',
	'Byte', 'Kilobyte', 'Megabyte',
]
