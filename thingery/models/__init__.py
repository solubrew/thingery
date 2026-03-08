# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Models
	description: >
		Unified data models for Thingery
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


# Element Category Enum
class ElementCategory(Enum):
    ALKALI_METAL = "alkali metal"
    ALKALINE_EARTH_METAL = "alkaline earth metal"
    TRANSITION_METAL = "transition metal"
    POST_TRANSITION_METAL = "post-transition metal"
    METALLOID = "metalloid"
    NONMETAL = "nonmetal"
    HALOGEN = "halogen"
    NOBLE_GAS = "noble gas"
    LANTHANIDE = "lanthanide"
    ACTINIDE = "actinide"


# Phase Enum
class Phase(Enum):
    SOLID = "solid"
    LIQUID = "liquid"
    GAS = "gas"
    PLASMA = "plasma"


# Decay Mode Enum
class DecayMode(Enum):
    STABLE = "stable"
    ALPHA = "alpha"
    BETA_MINUS = "beta_minus"
    BETA_PLUS = "beta_plus"
    ELECTRON_CAPTURE = "electron_capture"
    NEUTRON_EMISSION = "neutron_emission"
    PROTON_EMISSION = "proton_emission"
    SPONTANEOUS_FISSION = "spontaneous_fission"


# ======================================Element Models=============================================================||
# ====================================================================================================================||


@dataclass
class Isotope:
    """Isotope data model"""
    mass_number: int
    symbol: str
    atomic_mass: float
    abundance: Optional[float] = None  # Percentage
    half_life: Optional[float] = None  # Years
    decay_mode: Optional[str] = None


@dataclass
class Element:
    """Element data model"""
    atomic_number: int
    symbol: str
    name: str
    atomic_mass: float
    category: str
    phase: str
    density: float  # g/cm³
    melting_point: float  # Kelvin
    boiling_point: float  # Kelvin
    electron_config: str
    electronegativity: Optional[float] = None
    ionization_energy: Optional[float] = None  # kJ/mol
    isotopes: List[Isotope] = field(default_factory=list)


# ======================================Material Models=============================================================||
# ====================================================================================================================||


class MaterialCategory(Enum):
    METAL = "metal"
    ALLOY = "alloy"
    POLYMER = "polymer"
    CERAMIC = "ceramic"
    SEMICONDUCTOR = "semiconductor"
    COMPOSITE = "composite"
    FLUID = "fluid"
    GLASS = "glass"
    MINERAL = "mineral"
    CHEMICAL = "chemical"
    NANOMATERIAL = "nanomaterial"


@dataclass
class Material:
    """Material data model"""
    name: str
    formula: Optional[str]
    category: str
    density: float  # g/cm³
    melting_point: Optional[float] = None  # Kelvin
    boiling_point: Optional[float] = None  # Kelvin
    hardness: Optional[float] = None  # Mohs
    tensile_strength: Optional[float] = None  # MPa
    thermal_conductivity: Optional[float] = None  # W/(m·K)
    electrical_resistivity: Optional[float] = None  # Ω·m
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Alloy(Material):
    """Alloy data model"""
    components: Dict[str, float] = field(default_factory=dict)  # element: percentage


@dataclass
class Polymer(Material):
    """Polymer data model"""
    monomer: Optional[str] = None
    polymer_type: Optional[str] = None  # thermoplastic, thermoset, elastomer
    glass_transition_temp: Optional[float] = None  # Kelvin


@dataclass
class Ceramic(Material):
    """Ceramic data model"""
    crystal_structure: Optional[str] = None
    dielectric_strength: Optional[float] = None  # kV/mm


# ======================================Food Models=================================================================||
# ====================================================================================================================||


@dataclass
class Nutrition:
    """Nutrition data per 100g"""
    calories: float  # kcal
    protein: float  # g
    carbohydrates: float  # g
    fat: float  # g
    fiber: float  # g
    sugar: float  # g
    sodium: float  # mg
    cholesterol: float  # mg
    vitamins: Dict[str, float] = field(default_factory=dict)
    minerals: Dict[str, float] = field(default_factory=dict)


@dataclass
class Food:
    """Food data model"""
    name: str
    category: str
    serving_size: float  # grams
    nutrition: Nutrition
    amino_acids: Optional[Dict[str, float]] = None
    fatty_acids: Optional[Dict[str, float]] = None


# ======================================Institution Models===========================================================||
# ====================================================================================================================||


class InstitutionType(Enum):
    UNIVERSITY = "university"
    RESEARCH_LAB = "research_lab"
    COMPANY = "company"
    GOVERNMENT = "government"
    NONPROFIT = "nonprofit"


@dataclass
class Institution:
    """Institution data model"""
    name: str
    institution_type: str
    location: str  # City, Country
    founded: Optional[int] = None
    website: Optional[str] = None
    focus_areas: List[str] = field(default_factory=list)
    notable_research: List[str] = field(default_factory=list)


# ======================================Color Models=================================================================||
# ====================================================================================================================||


@dataclass
class Color:
    """Color data model"""
    name: str
    hex_code: str
    rgb: tuple = (0, 0, 0)
    hsl: tuple = (0, 0, 0)
    category: str = "web"


# ======================================Scale Models=================================================================||
# ====================================================================================================================||


@dataclass
class Scale:
    """Measurement scale data model"""
    name: str
    unit: str
    symbol: str
    category: str  # temperature, pressure, length, mass, etc.
    conversion_factor: Optional[float] = None
    base_unit: Optional[str] = None


# ======================================Protocol Models=============================================================||
# ====================================================================================================================||


@dataclass
class Protocol:
    """Protocol data model"""
    name: str
    category: str  # measurement, synthesis, analysis
    description: str
    steps: List[str] = field(default_factory=list)
    equipment: List[str] = field(default_factory=list)
    safety_notes: List[str] = field(default_factory=list)
    duration: Optional[str] = None


# ======================================Exports======================================================================||
# ====================================================================================================================||


__all__ = [
    'ElementCategory', 'Phase', 'DecayMode', 'MaterialCategory', 'InstitutionType',
    'Isotope', 'Element', 'Material', 'Alloy', 'Polymer', 'Ceramic',
    'Nutrition', 'Food', 'Institution', 'Color', 'Scale', 'Protocol'
]
