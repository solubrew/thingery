# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Hydrogen Element and Isotopes
	description: >
		Complete hydrogen data including all isotopes
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# ======================================Standard Library Modules======================================================||
from dataclasses import field
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
from thingery.models import Element, Isotope, ElementCategory, Phase, DecayMode

# ====================================================================================================================||

# Hydrogen isotopes
HYDROGEN_ISOTOPES = [
	# Protium (H-1) - most abundant
	Isotope(
		symbol="H",
		mass_number=1,
		atomic_mass=1.007825,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.999885,
		stable=True,
		neutrons=0,
		protons=1
	),
	# Deuterium (H-2)
	Isotope(
		symbol="D",
		mass_number=2,
		atomic_mass=2.014102,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.000115,
		stable=True,
		neutrons=1,
		protons=1
	),
	# Tritium (H-3)
	Isotope(
		symbol="T",
		mass_number=3,
		atomic_mass=3.016049,
		half_life=12.32,
		half_life_unit="y",
		decay_mode=DecayMode.BETA_MINUS,
		abundance=None,
		stable=False,
		neutrons=2,
		protons=1
	),
	# H-4 (quadrium)
	Isotope(
		symbol="H-4",
		mass_number=4,
		atomic_mass=4.027912,
		half_life=1.39e-22,
		half_life_unit="s",
		decay_mode=DecayMode.NEUTRON_EMISSION,
		stable=False,
		neutrons=3,
		protons=1
	),
	# H-5
	Isotope(
		symbol="H-5",
		mass_number=5,
		atomic_mass=5.035311,
		half_life=9.1e-23,
		half_life_unit="s",
		decay_mode=DecayMode.NEUTRON_EMISSION,
		stable=False,
		neutrons=4,
		protons=1
	),
	# H-6
	Isotope(
		symbol="H-6",
		mass_number=6,
		atomic_mass=6.044940,
		half_life=3.3e-27,
		half_life_unit="s",
		decay_mode=DecayMode.NEUTRON_EMISSION,
		stable=False,
		neutrons=5,
		protons=1
	),
	# H-7
	Isotope(
		symbol="H-7",
		mass_number=7,
		atomic_mass=7.053760,
		half_life=6.6e-27,
		half_life_unit="s",
		decay_mode=DecayMode.NEUTRON_EMISSION,
		stable=False,
		neutrons=6,
		protons=1
	),
]

# Hydrogen element
Hydrogen = Element(
	atomic_number=1,
	symbol="H",
	name="Hydrogen",
	atomic_mass=1.008,
	category=ElementCategory.NONMETAL.value,
	phase=Phase.GAS.value,
	density=0.00008988,
	melting_point=14.01,
	boiling_point=20.28,
	electron_config="1s1",
	electronegativity=2.20,
	ionization_energy=13.598,
	electron_affinity=72.8,
	atomic_radius=53,
	covalent_radius=31,
	van_der_waals_radius=120,
	oxidation_states=[-1, 1],
	isotopes=HYDROGEN_ISOTOPES,
	discovered_by="Henry Cavendish",
	year_discovered=1766,
	description="Hydrogen is the lightest element. It is the most abundant chemical substance in the universe."
)

__all__ = ['Hydrogen', 'HYDROGEN_ISOTOPES']
