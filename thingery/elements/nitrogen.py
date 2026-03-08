# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Nitrogen Element and Isotopes
	description: >
		Complete nitrogen data including all isotopes
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

# Nitrogen isotopes
NITROGEN_ISOTOPES = [
	# N-13 (unstable, PET imaging)
	Isotope(
		symbol="N-13",
		mass_number=13,
		atomic_mass=13.005739,
		half_life=9.97,
		half_life_unit="m",
		decay_mode=DecayMode.BETA_PLUS,
		stable=False,
		neutrons=6,
		protons=7
	),
	# N-14 (stable, most abundant)
	Isotope(
		symbol="N-14",
		mass_number=14,
		atomic_mass=14.003074,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.99632,
		stable=True,
		neutrons=7,
		protons=7
	),
	# N-15 (stable)
	Isotope(
		symbol="N-15",
		mass_number=15,
		atomic_mass=15.000109,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.00368,
		stable=True,
		neutrons=8,
		protons=7
	),
	# N-16 (unstable)
	Isotope(
		symbol="N-16",
		mass_number=16,
		atomic_mass=16.006099,
		half_life=7.13,
		half_life_unit="s",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=9,
		protons=7
	),
	# N-17 (unstable)
	Isotope(
		symbol="N-17",
		mass_number=17,
		atomic_mass=17.008450,
		half_life=4.17,
		half_life_unit="s",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=10,
		protons=7
	),
]

# Nitrogen element
Nitrogen = Element(
	atomic_number=7,
	symbol="N",
	name="Nitrogen",
	atomic_mass=14.007,
	category=ElementCategory.NONMETAL.value,
	phase=Phase.GAS.value,
	density=0.0012506,
	melting_point=63.15,
	boiling_point=77.36,
	electron_config="1s2 2s2 2p3",
	electronegativity=3.04,
	ionization_energy=14.534,
	electron_affinity=-7,
	atomic_radius=75,
	covalent_radius=71,
	oxidation_states=[-3, -2, -1, 1, 2, 3, 4, 5],
	isotopes=NITROGEN_ISOTOPES,
	discovered_by="Daniel Rutherford",
	year_discovered=1772,
	description="Nitrogen is a colorless, odorless gas that makes up about 78% of Earth's atmosphere."
)

__all__ = ['Nitrogen', 'NITROGEN_ISOTOPES']
