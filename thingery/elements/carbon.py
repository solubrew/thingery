# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Carbon Element and Isotopes
	description: >
		Complete carbon data including all isotopes
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

# Carbon isotopes
CARBON_ISOTOPES = [
	# C-8 through C-22 isotopes documented
	# C-11 (unstable, PET imaging)
	Isotope(
		symbol="C-11",
		mass_number=11,
		atomic_mass=11.011434,
		half_life=20.364,
		half_life_unit="m",
		decay_mode=DecayMode.BETA_PLUS,
		stable=False,
		neutrons=5,
		protons=6
	),
	# C-12 (stable, most abundant)
	Isotope(
		symbol="C-12",
		mass_number=12,
		atomic_mass=12.000000,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.9893,
		stable=True,
		neutrons=6,
		protons=6
	),
	# C-13 (stable)
	Isotope(
		symbol="C-13",
		mass_number=13,
		atomic_mass=13.003355,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.0107,
		stable=True,
		neutrons=7,
		protons=6
	),
	# C-14 (unstable, radiocarbon dating)
	Isotope(
		symbol="C-14",
		mass_number=14,
		atomic_mass=14.003242,
		half_life=5730,
		half_life_unit="y",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=8,
		protons=6
	),
	# C-15 (unstable)
	Isotope(
		symbol="C-15",
		mass_number=15,
		atomic_mass=15.010599,
		half_life=2.449,
		half_life_unit="s",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=9,
		protons=6
	),
	# C-16 (unstable)
	Isotope(
		symbol="C-16",
		mass_number=16,
		atomic_mass=16.014701,
		half_life=0.747,
		half_life_unit="s",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=10,
		protons=6
	),
]

# Carbon element
Carbon = Element(
	atomic_number=6,
	symbol="C",
	name="Carbon",
	atomic_mass=12.011,
	category=ElementCategory.NONMETAL.value,
	phase=Phase.SOLID.value,
	density=2.267,
	melting_point=3823,
	boiling_point=4098,
	electron_config="1s2 2s2 2p2",
	electronegativity=2.55,
	ionization_energy=11.260,
	electron_affinity=153.9,
	atomic_radius=77,
	covalent_radius=77,
	van_der_waals_radius=170,
	oxidation_states=[-4, -3, -2, -1, 1, 2, 3, 4],
	isotopes=CARBON_ISOTOPES,
	discovered_by="Ancient",
	year_discovered=None,
	description="Carbon is the basis of all known life. It forms more compounds than any other element."
)

__all__ = ['Carbon', 'CARBON_ISOTOPES']
