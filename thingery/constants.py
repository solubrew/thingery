# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Constants
	description: >
		Physical constants, mathematical constants, and universal values.
		Data loaded from constants.yaml for easy updates.
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
import math
from dataclasses import dataclass
from typing import Any, Dict, Optional

# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules==============================================||

# Import YAML loader
from thingery._loader import load_yaml, create_dataclass_from_dict


# ============================================================================
# Dataclasses for Type Safety
# ============================================================================


@dataclass
class Constant:
    """Represents a physical or mathematical constant."""
    name: str
    symbol: str
    value: Any
    unit: str
    description: str


# ============================================================================
# YAML Data Loading
# ============================================================================


def _load_constants() -> Dict[str, Constant]:
    """Load all constants from YAML."""
    data = load_yaml('constants.yaml')
    constants_data = data.get('constants', {})
    
    constants = {}
    for key, value in constants_data.items():
        constants[key] = Constant(
            name=value.get('name', key),
            symbol=value.get('symbol', ''),
            value=value.get('value'),
            unit=value.get('unit', ''),
            description=value.get('description', '')
        )
    return constants


# Load constants at module import time
_CONSTANTS: Dict[str, Constant] = _load_constants()


# ============================================================================
# Python Function API (Backward Compatible)
# ============================================================================


def avogadro() -> float:
    """Avogadro's Number (NA) = 6.02214076 × 10^23 mol^-1"""
    return _CONSTANTS['avogadro'].value


def boltzmann() -> float:
    """Boltzmann's Constant (k) = 1.380649 x 10^-23 J/K"""
    return _CONSTANTS['boltzmann'].value


def charge() -> float:
    """Elementary Charge (e) = 1.602176634 × 10^-19 C"""
    return _CONSTANTS['charge'].value


def speed_of_light() -> float:
    """Speed of light in meters / second (vacuum)"""
    return _CONSTANTS['speed_of_light'].value


def planks() -> float:
    """Planck's Constant (h) = 6.62607015 × 10^-34 m^2 kg / s"""
    return _CONSTANTS['planks'].value


def reduced_planks() -> float:
    """Reduced Planck Constant (ħ) = 1.054571817 × 10^-34 J s"""
    return _CONSTANTS['reduced_planks'].value


def gravitational_constant() -> float:
    """Gravitational Constant (G)"""
    return _CONSTANTS['gravitational_constant'].value


def gravitational_constant_earth() -> float:
    """Alias for gravitational_constant()"""
    return gravitational_constant()


def permittivity() -> float:
    """Permittivity of Free Space (ε0)"""
    return _CONSTANTS['permittivity'].value


def permeability() -> float:
    """Permeability of Free Space (μ0)"""
    return _CONSTANTS['permeability'].value


def stefan_boltzmann() -> float:
    """Stefan-Boltzmann Constant (σ)"""
    return _CONSTANTS['stefan_boltzmann'].value


def rydberg() -> float:
    """Rydberg Constant (R∞)"""
    return _CONSTANTS['rydberg'].value


def faraday() -> float:
    """Faraday Constant (F)"""
    return _CONSTANTS['faraday'].value


def ideal_gas() -> float:
    """Ideal Gas Constant (R) = 8.314462618 J/(mol·K)"""
    return _CONSTANTS['gas_constant'].value


def electron_mass() -> float:
    """Electron Mass (me)"""
    return _CONSTANTS['electron_mass'].value


def proton_mass() -> float:
    """Proton Mass (mp)"""
    return _CONSTANTS['proton_mass'].value


def neutron_mass() -> float:
    """Neutron Mass (mn)"""
    return _CONSTANTS['neutron_mass'].value


def atomic_mass_unit() -> float:
    """Atomic Mass Unit (u)"""
    return _CONSTANTS['atomic_mass_unit'].value


# Mathematical constants
def e() -> float:
    """Euler's Number (e)"""
    return _CONSTANTS['e'].value


def pi() -> float:
    """Pi (π)"""
    return _CONSTANTS['pi'].value


def phi() -> float:
    """Golden Ratio (φ)"""
    return _CONSTANTS['phi'].value


def sqrt2() -> float:
    """Square Root of 2 (√2)"""
    return _CONSTANTS['sqrt2'].value


def sqrt3() -> float:
    """Square Root of 3 (√3)"""
    return _CONSTANTS['sqrt3'].value


def tao() -> float:
    """Tau (τ) = 2π"""
    return _CONSTANTS['pi'].value * 2


def primes() -> list:
    """List of known primes (placeholder - could be expanded from YAML)"""
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


# Earth & Planetary constants
def earth_mass() -> float:
    """Earth Mass"""
    return _CONSTANTS['earth_mass'].value


def earth_radius() -> float:
    """Earth Radius"""
    return _CONSTANTS['earth_radius'].value


def earth_surface_gravity() -> float:
    """Earth Surface Gravity"""
    return _CONSTANTS['earth_surface_gravity'].value


def earth_atmosphere() -> float:
    """Standard Atmosphere"""
    return _CONSTANTS['earth_atmosphere'].value


def moon_mass() -> float:
    """Moon Mass"""
    return _CONSTANTS['moon_mass'].value


def solar_mass() -> float:
    """Solar Mass"""
    return _CONSTANTS['solar_mass'].value


def solar_luminosity() -> float:
    """Solar Luminosity"""
    return _CONSTANTS['solar_luminosity'].value


def astronomical_unit() -> float:
    """Astronomical Unit (AU)"""
    return _CONSTANTS['astronomical_unit'].value


# Particle Physics
def fine_structure() -> float:
    """Fine-Structure Constant (α)"""
    return _CONSTANTS['fine_structure'].value


def weak_mixing_angle() -> float:
    """Weinberg Angle (θW)"""
    return _CONSTANTS['weak_mixing_angle'].value


# Time constants
def planck_time() -> float:
    """Planck Time"""
    return _CONSTANTS['planck_time'].value


def planck_length() -> float:
    """Planck Length"""
    return _CONSTANTS['planck_length'].value


def planck_temperature() -> float:
    """Planck Temperature"""
    return _CONSTANTS['planck_temperature'].value


# Standard conditions
def standard_temperature() -> float:
    """Standard Temperature (0°C in Kelvin)"""
    return _CONSTANTS['standard_temperature'].value


def standard_pressure() -> float:
    """Standard Pressure (1 atm in Pascals)"""
    return _CONSTANTS['standard_pressure'].value


def absolute_zero() -> float:
    """Absolute Zero (°C)"""
    return _CONSTANTS['absolute_zero'].value


def triple_point_water() -> float:
    """Triple Point of Water (K)"""
    return _CONSTANTS['triple_point_water'].value


# ============================================================================
# Direct Data Access
# ============================================================================


def get_constant(name: str) -> Optional[Constant]:
    """Get a constant by name."""
    return _CONSTANTS.get(name)


def get_all_constants() -> Dict[str, Constant]:
    """Get all constants as a dictionary."""
    return _CONSTANTS.copy()


def list_constant_names() -> list:
    """List all available constant names."""
    return list(_CONSTANTS.keys())


# ============================================================================
# Exports
# ============================================================================


__all__ = [
    # Function API
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
    # Data access
    'Constant', 'get_constant', 'get_all_constants', 'list_constant_names',
]
