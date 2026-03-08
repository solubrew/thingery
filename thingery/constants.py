# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name:
	description: >
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# ======================================Standard Library Modules======================================================||
from os.path import abspath, dirname, join
import math

# ======================================3rd Party Library Modules=====================================================||

# ======================================Solutions Brewer Library Modules==============================================||
from condor import condor
from ogma.logma import Logma

# ====================================================================================================================||
here = join(dirname(__file__), '')  # ||
logma = Logma(__name__)

# ====================================================================================================================||
pxcfg = join(here, '_data_', '.yaml')

def avogadro():
	"""Avogadro's Number (NA) = 6.02214076 × 10^23 mol^-1, represents the number of particles in one mole."""
	return 60221407600000000000000

def boltzmann():
	"""Boltzmann's Constant (k) = 1.380649 x 10^-23 J/K, relates energy to temperature."""
	return 0.00000000000000000000001380649

def charge():
	"""Elementary Charge (e) = 1.602176634 × 10^-19 C, the charge of an electron."""
	return 0.0000000000000000001602176634

def e():
	""""""
	return math.e

def gravitational_constant_earth():
	"""Gravitation constant in meters cubed / kilogram second squared"""
	return 0.0000000000667430

def ideal_gas():
	"""Ideal Gas Constant (R) = 8.314462618 J/(mol·K), the constant in the ideal gas law"""
	return 8.314462618

def phi():
	""""""
	return (1 + math.sqrt(5)) / 2

def pi():
	""""""
	return math.pi

def tao():
	""""""
	return pi() * 2

def primes():
	"""return list of known primes"""

def speed_of_light():
	"""Speed of light in meters / second as measured in a vacuum as per 2024 physics"""
	return 299792458

def permeability():
	"""Permeability of Free Space (μ0) = 4π × 10^-7 T m/A."""
	return 4 * pi() * 0.0000001

def permittivity():
	"""Permittivity of Free Space (ε0) = 8.8541878128(13) x 10^-12 F/m."""
	return 0.0000000000088541878128

def planks():
	"""Planck's Constant (h) = 6.62607015 × 10^-34 m^2 kg / s, fundamental constant of quantum mechanics."""
	return 0.000000000000000000000000000000000662607015


# ====================================================================================================================||

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||