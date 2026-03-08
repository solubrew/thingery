# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Copper Element and Isotopes
	description: >
		Complete copper data including all isotopes
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
from thingery.models import Element, Isotope, ElementCategory, Phase, DecayMode

# ====================================================================================================================||

# Copper isotopes
COPPER_ISOTOPES = [
	# Cu-52 through Cu-69
	# Cu-63 (stable, most abundant)
	Isotope(
		symbol="Cu-63",
		mass_number=63,
		atomic_mass=62.929601,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.6915,
		stable=True,
		neutrons=34,
		protons=29
	),
	# Cu-65 (stable)
	Isotope(
		symbol="Cu-65",
		mass_number=65,
		atomic_mass=64.927789,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.3085,
		stable=True,
		neutrons=36,
		protons=29
	),
	# Cu-64 (unstable)
	Isotope(
		symbol="Cu-64",
		mass_number=64,
		atomic_mass=63.929764,
		half_life=12.7,
		half_life_unit="h",
		decay_mode=DecayMode.BETA_PLUS,
		stable=False,
		neutrons=35,
		protons=29
	),
	# Cu-67 (unstable)
	Isotope(
		symbol="Cu-67",
		mass_number=67,
		atomic_mass=66.927730,
		half_life=61.9,
		half_life_unit="h",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=38,
		protons=29
	),
]

# Copper element
Copper = Element(
	atomic_number=29,
	symbol="Cu",
	name="Copper",
	atomic_mass=63.546,
	category=ElementCategory.TRANSITION_METAL.value,
	phase=Phase.SOLID.value,
	density=8960,
	melting_point=1357.77,
	boiling_point=2835,
	electron_config="[Ar] 3d10 4s1",
	electronegativity=1.90,
	ionization_energy=7.726,
	electron_affinity=118.4,
	atomic_radius=145,
	covalent_radius=132,
	van_der_waals_radius=140,
	oxidation_states=[1, 2, 3],
	isotopes=COPPER_ISOTOPES,
	discovered_by="Ancient",
	year_discovered=None,
	description="Copper is a soft, malleable, and ductile metal with very high thermal and electrical conductivity."
)

__all__ = ['Copper', 'COPPER_ISOTOPES']
