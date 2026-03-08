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

# Institutions - YAML-based loading with backward compatibility
from thingery.institutions import institutions as _inst
# New YAML-based exports
from thingery.institutions.institutions import (
	all_institutions, banks, government, universities, international_orgs, 
	corporations, established,
	load_institutions, get_institutions_by_type, get_institutions_by_founded, get_institution
)

# Colors - backward compatible imports + new functions
from thingery.colors import (
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
	
	# Institutions - YAML-based
	'all_institutions', 'banks', 'government', 'universities', 'international_orgs',
	'corporations', 'established',
	'load_institutions', 'get_institutions_by_type', 'get_institutions_by_founded', 'get_institution',
	
	# Colors
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