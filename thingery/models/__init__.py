# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Data Models
	description: >
		Comprehensive data models for all Thingery categories
		including Elements, Isotopes, Materials, Food, Institutions, Colors, Scales, and Protocols
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# ======================================Standard Library Modules======================================================||
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, Tuple
from enum import Enum

# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||

# Element Categories
class ElementCategory(str, Enum):
	"""Element categories"""
	ALKALI_METAL = "alkali_metal"
	ALKALINE_EARTH_METAL = "alkaline_earth_metal"
	TRANSITION_METAL = "transition_metal"
	POST_TRANSITION_METAL = "post_transition_metal"
	METALLOID = "metalloid"
	NONMETAL = "nonmetal"
	HALOGEN = "halogen"
	NOBLE_GAS = "noble_gas"
	LANTHANIDE = "lanthanide"
	ACTINIDE = "actinide"

# Phase at standard conditions
class Phase(str, Enum):
	"""Physical phase at STP"""
	SOLID = "solid"
	LIQUID = "liquid"
	GAS = "gas"
	UNKNOWN = "unknown"

# Decay modes
class DecayMode(str, Enum):
	"""Radioactive decay modes"""
	ALPHA = "alpha"
	BETA_MINUS = "beta_minus"
	BETA_PLUS = "beta_plus"
	GAMMA = "gamma"
	NEUTRON_EMISSION = "neutron_emission"
	SPONTANEOUS_FISSION = "spontaneous_fission"
	STABLE = "stable"

# Material categories
class MaterialCategory(str, Enum):
	"""Material categories"""
	METAL = "metal"
	ALLOY = "alloy"
	POLYMER = "polymer"
	CERAMIC = "ceramic"
	COMPOSITE = "composite"
	SEMICONDUCTOR = "semiconductor"
	INSULATOR = "insulator"
	FLUID = "fluid"
	BIOMATERIAL = "biomaterial"

# Institution types
class InstitutionType(str, Enum):
	"""Types of institutions"""
	UNIVERSITY = "university"
	RESEARCH_LAB = "research_lab"
	GOVERNMENT = "government"
	INDUSTRY = "industry"
	HOSPITAL = "hospital"
	MUSEUM = "museum"
	LIBRARY = "library"

# Food categories
class FoodCategory(str, Enum):
	"""Food categories"""
	FRUIT = "fruit"
	VEGETABLE = "vegetable"
	GRAIN = "grain"
	PROTEIN = "protein"
	DAIRY = "dairy"
	FAT = "fat"
	BEVERAGE = "beverage"
	SNACK = "snack"
	CONDIMENT = "condiment"
	SPICE = "spice"

# ====================================================================================================================||
# Element Models
# ====================================================================================================================||

@dataclass
class Isotope:
	"""Isotope data model"""
	symbol: str
	mass_number: int
	atomic_mass: float
	half_life: Optional[float] = None  # in seconds, None if stable
	half_life_unit: Optional[str] = None  # s, m, h, d, y
	decay_mode: str = DecayMode.STABLE.value
	abundance: Optional[float] = None  # decimal percentage
	stable: bool = True
	neutrons: int = 0
	protons: int = 0

	def __post_init__(self):
		if self.half_life is not None:
			self.stable = False

@dataclass
class ElectronConfiguration:
	"""Electron configuration"""
	notation: str  # e.g., "1s2 2s2 2p6"
	shells: List[int] = field(default_factory=list)  # [2, 8, 18, 32, 32, 18, 8]

@dataclass
class Element:
	"""Element data model"""
	atomic_number: int
	symbol: str
	name: str
	atomic_mass: float
	category: str  # ElementCategory value
	phase: str  # Phase value
	density: float  # kg/m³
	melting_point: float  # Kelvin
	boiling_point: float  # Kelvin
	electron_config: str
	electronegativity: Optional[float] = None
	ionization_energy: Optional[float] = None  # eV
	electron_affinity: Optional[float] = None  # eV
	atomic_radius: Optional[float] = None  # pm
	covalent_radius: Optional[float] = None  # pm
	van_der_waals_radius: Optional[float] = None  # pm
	oxidation_states: List[int] = field(default_factory=list)
	isotopes: List[Isotope] = field(default_factory=list)
	discovered_by: Optional[str] = None
	year_discovered: Optional[int] = None
	description: str = ""

	def __post_init__(self):
		for iso in self.isotopes:
			iso.protons = self.atomic_number
			iso.neutrons = iso.mass_number - self.atomic_number

# ====================================================================================================================||
# Material Models
# ====================================================================================================================||

@dataclass
class MaterialProperty:
	"""Material property with value and unit"""
	name: str
	value: float
	unit: str
	temperature: Optional[float] = None  # Kelvin

@dataclass
class Material:
	"""Material data model"""
	name: str
	formula: Optional[str]
	category: str  # MaterialCategory value
	density: float  # kg/m³
	melting_point: Optional[float] = None  # Kelvin
	boiling_point: Optional[float] = None  # Kelvin
	properties: List[MaterialProperty] = field(default_factory=list)
	composition: Dict[str, float] = field(default_factory=dict)  # element: percentage
	description: str = ""
	color: Optional[str] = None
	hardness: Optional[str] = None
	tensile_strength: Optional[float] = None  # MPa
	youngs_modulus: Optional[float] = None  # GPa
	electrical_conductivity: Optional[float] = None  # S/m
	thermal_conductivity: Optional[float] = None  # W/(m·K)

@dataclass
class Alloy(Material):
	"""Alloy data model"""
	components: List[Tuple[str, float]] = field(default_factory=list)  # (element, percentage)
	base_element: str = ""

@dataclass
class Composite(Material):
	"""Composite material data model"""
	matrix: str = ""
	reinforcement: str = ""
	fiber_orientation: Optional[str] = None
	volume_fraction: Optional[float] = None

# ====================================================================================================================||
# Food Models
# ====================================================================================================================||

@dataclass
class NutritionInfo:
	"""Nutrition information per 100g"""
	calories: float = 0
	protein: float = 0  # g
	carbohydrates: float = 0  # g
	fat: float = 0  # g
	fiber: float = 0  # g
	sugar: float = 0  # g
	sodium: float = 0  # mg
	cholesterol: float = 0  # mg
	vitamin_a: Optional[float] = None  # IU
	vitamin_c: Optional[float] = None  # mg
	calcium: Optional[float] = None  # mg
	iron: Optional[float] = None  # mg
	potassium: Optional[float] = None  # mg

@dataclass
class Food:
	"""Food data model"""
	name: str
	category: str  # FoodCategory value
	nutrition: NutritionInfo = field(default_factory=NutritionInfo)
	serving_size: float = 100  # g
	serving_unit: str = "g"
	aliases: List[str] = field(default_factory=list)
	description: str = ""
	is_raw: bool = True
	shelf_life: Optional[float] = None  # days
	storage_temp: Optional[float] = None  # Celsius

# ====================================================================================================================||
# Institution Models
# ====================================================================================================================||

@dataclass
class Institution:
	"""Institution data model"""
	name: str
	type: str  # InstitutionType value
	location: str  # City, Country
	coordinates: Optional[Tuple[float, float]] = None  # lat, lon
	established: Optional[int] = None  # year
	website: Optional[str] = None
	description: str = ""
	research_areas: List[str] = field(default_factory=list)
	notable_people: List[str] = field(default_factory=list)

# ====================================================================================================================||
# Color Models
# ====================================================================================================================||

@dataclass
class Color:
	"""Color data model"""
	name: str
	hex_code: str
	rgb: Tuple[int, int, int]
	hsl: Tuple[int, int, int]  # H: 0-360, S: 0-100, L: 0-100
	cmyk: Tuple[int, int, int, int]
	category: str = ""  # primary, secondary, tertiary, etc.
	aliases: List[str] = field(default_factory=list)

# ====================================================================================================================||
# Scale Models
# ====================================================================================================================||

@dataclass
class Scale:
	"""Measurement scale data model"""
	name: str
	abbreviation: str
	description: str
	type: str  # temperature, length, mass, etc.
	units: List[str] = field(default_factory=list)
	min_value: Optional[float] = None
	max_value: Optional[float] = None
	conversions: Dict[str, float] = field(default_factory=dict)  # unit: conversion_factor_to_base

@dataclass
class Unit:
	"""Unit of measurement"""
	name: str
	symbol: str
	scale_type: str
	to_base: float  # multiply by this to convert to base unit
	base_unit: str

# ====================================================================================================================||
# Protocol Models
# ====================================================================================================================||

@dataclass
class ProtocolStep:
	"""Step in a protocol"""
	step_number: int
	instruction: str
	duration: Optional[float] = None  # seconds
	temperature: Optional[float] = None  # Celsius
	pressure: Optional[float] = None  # Pa
	equipment: List[str] = field(default_factory=list)
	safety_notes: str = ""

@dataclass
class Protocol:
	"""Protocol data model"""
	name: str
	category: str  # synthesis, analysis, measurement, etc.
	description: str
	steps: List[ProtocolStep] = field(default_factory=list)
	materials_needed: List[str] = field(default_factory=list)
	equipment_needed: List[str] = field(default_factory=list)
	estimated_duration: Optional[float] = None  # seconds
	difficulty: str = "intermediate"  # beginner, intermediate, advanced
	safety_level: str = "moderate"  # low, moderate, high
	references: List[str] = field(default_factory=list)

# ====================================================================================================================||
# Export all models
# ====================================================================================================================||

__all__ = [
	# Enums
	'ElementCategory', 'Phase', 'DecayMode', 'MaterialCategory',
	'InstitutionType', 'FoodCategory',
	# Element models
	'Isotope', 'ElectronConfiguration', 'Element',
	# Material models
	'MaterialProperty', 'Material', 'Alloy', 'Composite',
	# Food models
	'NutritionInfo', 'Food',
	# Institution models
	'Institution',
	# Color models
	'Color',
	# Scale models
	'Scale', 'Unit',
	# Protocol models
	'ProtocolStep', 'Protocol',
]
