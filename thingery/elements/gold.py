# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Gold Element and Isotopes
	description: >
		Complete gold data including all isotopes
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

# Gold isotopes
GOLD_ISOTOPES = [
	# Au-197 (stable, only stable isotope)
	Isotope(
		symbol="Au-197",
		mass_number=197,
		atomic_mass=196.966552,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=1.0,
		stable=True,
		neutrons=118,
		protons=79
	),
	# Au-195 (unstable)
	Isotope(
		symbol="Au-195",
		mass_number=195,
		atomic_mass=194.965035,
		half_life=186,
		half_life_unit="d",
		decay_mode=DecayMode.ELECTRON_CAPTURE,
		stable=False,
		neutrons=116,
		protons=79
	),
	# Au-198 (unstable)
	Isotope(
		symbol="Au-198",
		mass_number=198,
		atomic_mass=197.968217,
		half_life=2.696,
		half_life_unit="d",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=119,
		protons=79
	),
	# Au-199 (unstable)
	Isotope(
		symbol="Au-199",
		mass_number=199,
		atomic_mass=198.968748,
		half_life=3.139,
		half_life_unit="d",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=120,
		protons=79
	),
	# Au-196 (unstable)
	Isotope(
		symbol="Au-196",
		mass_number=196,
		atomic_mass=195.966571,
		half_life=6.166,
		half_life_unit="d",
		decay_mode=DecayMode.ELECTRON_CAPTURE,
		stable=False,
		neutrons=117,
		protons=79
	),
]

# Gold element
Gold = Element(
	atomic_number=79,
	symbol="Au",
	name="Gold",
	atomic_mass=196.967,
	category=ElementCategory.TRANSITION_METAL.value,
	phase=Phase.SOLID.value,
	density=19300,
	melting_point=1337.33,
	boiling_point=3129,
	electron_config="[Xe] 4f14 5d10 6s1",
	electronegativity=2.54,
	ionization_energy=9.226,
	electron_affinity=222.8,
	atomic_radius=174,
	covalent_radius=136,
	van_waals_radius=166,
	oxidation_states=[-1, 1, 2, 3, 5],
	isotopes=GOLD_ISOTOPES,
	discovered_by="Ancient",
	year_discovered=None,
	description="Gold is a bright, slightly reddish yellow, dense, soft, malleable, and ductile metal."
)

__all__ = ['Gold', 'GOLD_ISOTOPES']
