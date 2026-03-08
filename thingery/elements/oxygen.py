# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Oxygen Element and Isotopes
	description: >
		Complete oxygen data including all isotopes
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

# Oxygen isotopes
OXYGEN_ISOTOPES = [
	# O-12 (unstable)
	Isotope(
		symbol="O-12",
		mass_number=12,
		atomic_mass=12.034405,
		half_life=5.8e-21,
		half_life_unit="s",
		decay_mode=DecayMode.NEUTRON_EMISSION,
		stable=False,
		neutrons=4,
		protons=8
	),
	# O-13 (unstable)
	Isotope(
		symbol="O-13",
		mass_number=13,
		atomic_mass=13.017812,
		half_life=8.58,
		half_life_unit="ms",
		decay_mode=DecayMode.BETA_PLUS,
		stable=False,
		neutrons=5,
		protons=8
	),
	# O-14 (unstable)
	Isotope(
		symbol="O-14",
		mass_number=14,
		atomic_mass=14.008596,
		half_life=70.598,
		half_life_unit="s",
		decay_mode=DecayMode.BETA_PLUS,
		stable=False,
		neutrons=6,
		protons=8
	),
	# O-15 (unstable)
	Isotope(
		symbol="O-15",
		mass_number=15,
		atomic_mass=15.003065,
		half_life=122.24,
		half_life_unit="s",
		decay_mode=DecayMode.BETA_PLUS,
		stable=False,
		neutrons=7,
		protons=8
	),
	# O-16 (stable, most abundant)
	Isotope(
		symbol="O-16",
		mass_number=16,
		atomic_mass=15.994915,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.99757,
		stable=True,
		neutrons=8,
		protons=8
	),
	# O-17 (stable)
	Isotope(
		symbol="O-17",
		mass_number=17,
		atomic_mass=16.999132,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.00038,
		stable=True,
		neutrons=9,
		protons=8
	),
	# O-18 (stable)
	Isotope(
		symbol="O-18",
		mass_number=18,
		atomic_mass=17.999160,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.00205,
		stable=True,
		neutrons=10,
		protons=8
	),
	# O-19 (unstable)
	Isotope(
		symbol="O-19",
		mass_number=19,
		atomic_mass=19.003580,
		half_life=26.91,
		half_life_unit="s",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=11,
		protons=8
	),
	# O-20 (unstable)
	Isotope(
		symbol="O-20",
		mass_number=20,
		atomic_mass=20.004077,
		half_life=13.51,
		half_life_unit="s",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=12,
		protons=8
	),
]

# Oxygen element
Oxygen = Element(
	atomic_number=8,
	symbol="O",
	name="Oxygen",
	atomic_mass=15.999,
	category=ElementCategory.NONMETAL.value,
	phase=Phase.GAS.value,
	density=0.001429,
	melting_point=54.36,
	boiling_point=90.20,
	electron_config="1s2 2s2 2p4",
	electronegativity=3.44,
	ionization_energy=13.618,
	electron_affinity=141,
	atomic_radius=73,
	covalent_radius=66,
	van_der_waals_radius=152,
	oxidation_states=[-2, -1, 1, 2],
	isotopes=OXYGEN_ISOTOPES,
	discovered_by="Carl Wilhelm Scheele",
	year_discovered=1774,
	description="Oxygen is a colorless, odorless, tasteless gas essential for respiration."
)

__all__ = ['Oxygen', 'OXYGEN_ISOTOPES']
