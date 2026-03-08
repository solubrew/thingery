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

# Materials - new YAML-based module
from thingery.materials import (
	get_material, list_materials, list_categories, search_materials
)

# Foods - YAML-based loading (no individual class exports - use get_food() instead)
from thingery.food import (
	get_food,
	get_food_or_raise,
	list_foods,
	list_categories,
	get_foods_by_category,
	search_foods,
	Food,
)

# Institutions - YAML-based loading with backward compatibility
from thingery.institutions import institutions as _inst
# New YAML-based exports
from thingery.institutions.institutions import (
	all_institutions, banks, government, universities, international_orgs, 
	corporations, established,
	load_institutions, get_institutions_by_type, get_institutions_by_founded, get_institution
)

# Institutions Archive - institutions founded after 1926 (younger than 100 years)
from thingery.institutions_archive import (
	all_institutions as archive_institutions,
	banks as archive_banks,
	government_labs,
	international_orgs as archive_international_orgs,
	corporations as archive_corporations,
	younger_than_100,
	load_institutions as load_archived_institutions
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
	
	# Foods - use get_food() to access individual foods
	'get_food',
	'get_food_or_raise',
	'list_foods',
	'list_categories',
	'get_foods_by_category',
	'search_foods',
	'Food',
	
	# Institutions - YAML-based
	'all_institutions', 'banks', 'government', 'universities', 'international_orgs',
	'corporations', 'established',
	'load_institutions', 'get_institutions_by_type', 'get_institutions_by_founded', 'get_institution',
	
	# Institutions Archive - younger than 100 years
	'archive_institutions', 'archive_banks', 'government_labs', 
	'archive_international_orgs', 'archive_corporations', 'younger_than_100',
	'load_archived_institutions',
	
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