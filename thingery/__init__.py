# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery
	description: >
		Thingery - Physical/Chemical Data Library
		Complete database of elements, materials, foods, institutions, colors, scales, and protocols
		Data loaded from YAML configs for easy updates and expansion.
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

# Colors - backward compatible imports + new functions
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
	Viridian, RawUmber, BurntSienna, Ultramarine, PhthaloBlue,
	# New exports
	Color as ThingeryColor, get_color, get_Color, get_colors_by_category,
	list_categories as list_color_categories, list_colors
)

from thingery.pantone import (
	PantoneYellow, PantoneGoldenYellow, PantoneOrange, PantoneWarmRed,
	PantoneRed, PantoneRubineRed, PantoneRhodamineRed, PantoneMagenta,
	PantoneViolet, PantoneBlue, PantoneProcessBlue, PantoneGreen,
	PantoneBlack, PantoneCoolGray1, PantoneCoolGray5, PantoneCoolGray10,
	PantonePlusYellow, PantonePlusOrange021, PantonePlusWarmRed,
	PantonePlusRed, PantonePlusPink, PantonePlusRhodamineRed,
	PantonePlusPurple, PantonePlusViolet, PantonePlusBlue072,
	PantonePlusProcessBlue, PantonePlusGreen, PantonePlusBlack,
	PantoneMetallicGold, PantoneMetallicSilver,
	PantoneSkintoneLight, PantoneSkintoneMedium, PantoneSkintoneDark,
	PantoneFashionLilac, PantoneFashionBlue, PantoneFashionFuchsia,
	PantoneFashionEmerald, PantoneFashionTangerine
)

# Scales - backward compatible imports + new functions
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
	Byte, Kilobyte, Megabyte,
	# New exports
	get_scale, get_scales_by_category,
	list_categories as list_scale_categories, list_scales
)

# Protocols - new exports
from thingery.protocols import (
	Protocol, get_protocol, get_Protocol, get_protocols_by_category,
	list_categories as list_protocol_categories, list_protocols
)

# Constants - backward compatible imports + new
from thingery.constants import (
	avogadro, boltzmann, charge, speed_of_light,
	planks, reduced_planks, gravitational_constant, gravitational_constant_earth,
	permittivity, permeability, stefan_boltzmann, rydberg, faraday,
	ideal_gas, electron_mass, proton_mass, neutron_mass, atomic_mass_unit,
	e, pi, phi, sqrt2, sqrt3, tao, primes,
	earth_mass, earth_radius, earth_surface_gravity, earth_atmosphere,
	moon_mass, solar_mass, solar_luminosity, astronomical_unit,
	fine_structure, weak_mixing_angle,
	planck_time, planck_length, planck_temperature,
	standard_temperature, standard_pressure, absolute_zero, triple_point_water,
	# New exports
	Constant, get_constant, get_all_constants, list_constant_names
)

# YAML Loader
from thingery._loader import (
	ThingeryLoader, get_loader, load_yaml, load_category,
	create_dataclass_from_dict, create_dataclasses_from_list,
	DATA_DIR, THINGERY_DIR
)

# ====================================================================================================================||


__version__ = "0.1.0"

__all__ = [
	# Version
	'__version__',
	
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
	'ThingeryColor', 'get_color', 'get_Color', 'get_colors_by_category', 'list_colors',
	
	# Pantone Colors
	'PantoneYellow', 'PantoneGoldenYellow', 'PantoneOrange', 'PantoneWarmRed',
	'PantoneRed', 'PantoneRubineRed', 'PantoneRhodamineRed', 'PantoneMagenta',
	'PantoneViolet', 'PantoneBlue', 'PantoneProcessBlue', 'PantoneGreen',
	'PantoneBlack', 'PantoneCoolGray1', 'PantoneCoolGray5', 'PantoneCoolGray10',
	'PantonePlusYellow', 'PantonePlusOrange021', 'PantonePlusWarmRed',
	'PantonePlusRed', 'PantonePlusPink', 'PantonePlusRhodamineRed',
	'PantonePlusPurple', 'PantonePlusViolet', 'PantonePlusBlue072',
	'PantonePlusProcessBlue', 'PantonePlusGreen', 'PantonePlusBlack',
	'PantoneMetallicGold', 'PantoneMetallicSilver',
	'PantoneSkintoneLight', 'PantoneSkintoneMedium', 'PantoneSkintoneDark',
	'PantoneFashionLilac', 'PantoneFashionBlue', 'PantoneFashionFuchsia',
	'PantoneFashionEmerald', 'PantoneFashionTangerine',
	
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
	'get_scale', 'get_scales_by_category', 'list_scales',
	
	# Protocols
	'Protocol', 'get_protocol', 'get_Protocol', 'get_protocols_by_category', 'list_protocols',
	
	# Constants
	'avogadro', 'boltzmann', 'charge', 'speed_of_light',
	'planks', 'reduced_planks', 'gravitational_constant', 'gravitational_constant_earth',
	'permittivity', 'permeability', 'stefan_boltzmann', 'rydberg', 'faraday',
	'ideal_gas', 'electron_mass', 'proton_mass', 'neutron_mass', 'atomic_mass_unit',
	'e', 'pi', 'phi', 'sqrt2', 'sqrt3', 'tao', 'primes',
	'earth_mass', 'earth_radius', 'earth_surface_gravity', 'earth_atmosphere',
	'moon_mass', 'solar_mass', 'solar_luminosity', 'astronomical_unit',
	'fine_structure', 'weak_mixing_angle',
	'planck_time', 'planck_length', 'planck_temperature',
	'standard_temperature', 'standard_pressure', 'absolute_zero', 'triple_point_water',
	'Constant', 'get_constant', 'get_all_constants', 'list_constant_names',
	
	# YAML Loader
	'ThingeryLoader', 'get_loader', 'load_yaml', 'load_category',
	'create_dataclass_from_dict', 'create_dataclasses_from_list',
	'DATA_DIR', 'THINGERY_DIR',
]
