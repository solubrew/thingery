# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Silver Element and Isotopes
	description: >
		Complete silver data including all isotopes
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

# Silver isotopes
SILVER_ISOTOPES = [
	# Ag-107 (stable)
	Isotope(
		symbol="Ag-107",
		mass_number=107,
		atomic_mass=106.905097,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.51839,
		stable=True,
		neutrons=60,
		protons=47
	),
	# Ag-109 (stable)
	Isotope(
		symbol="Ag-109",
		mass_number=109,
		atomic_mass=108.904752,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.48161,
		stable=True,
		neutrons=62,
		protons=47
	),
	# Ag-105 (unstable)
	Isotope(
		symbol="Ag-105",
		mass_number=105,
		atomic_mass=104.906529,
		half_life=41.29,
		half_life_unit="d",
		decay_mode=DecayMode.ELECTRON_CAPTURE,
		stable=False,
		neutrons=58,
		protons=47
	),
	# Ag-108 (unstable)
	Isotope(
		symbol="Ag-108",
		mass_number=108,
		atomic_mass=107.905956,
		half_life=2.37,
		half_life_unit="m",
		decay_mode=DecayMode.BETA_PLUS,
		stable=False,
		neutrons=61,
		protons=47
	),
	# Ag-110 (unstable)
	Isotope(
		symbol="Ag-110",
		mass_number=110,
		atomic_mass=109.906111,
		half_life=24.6,
		half_life_unit="s",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=63,
		protons=47
	),
	# Ag-111 (unstable)
	Isotope(
		symbol="Ag-111",
		mass_number=111,
		atomic_mass=110.907291,
		half_life=7.45,
		half_life_unit="d",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=64,
		protons=47
	),
]

# Silver element
Silver = Element(
	atomic_number=47,
	symbol="Ag",
	name="Silver",
	atomic_mass=107.868,
	category=ElementCategory.TRANSITION_METAL.value,
	phase=Phase.SOLID.value,
	density=10500,
	melting_point=1234.93,
	boiling_point=2435,
	electron_config="[Kr] 4d10 5s1",
	electronegativity=1.93,
	ionization_energy=7.576,
	electron_affinity=125.6,
	atomic_radius=165,
	covalent_radius=145,
	van_der_waals_radius=172,
	oxidation_states=[1, 2, 3],
	isotopes=SILVER_ISOTOPES,
	discovered_by="Ancient",
	year_discovered=None,
	description="Silver is a soft, white, lustrous transition metal with the highest electrical conductivity."
)

__all__ = ['Silver', 'SILVER_ISOTOPES']
