# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Helium Element and Isotopes
	description: >
		Complete helium data including all isotopes
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

# Helium isotopes
HELIUM_ISOTOPES = [
	# He-3 (stable)
	Isotope(
		symbol="He-3",
		mass_number=3,
		atomic_mass=3.016029,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.00000134,
		stable=True,
		neutrons=1,
		protons=2
	),
	# He-4 (alpha particle, most abundant)
	Isotope(
		symbol="He-4",
		mass_number=4,
		atomic_mass=4.002603,
		half_life=None,
		decay_mode=DecayMode.STABLE,
		abundance=0.99999866,
		stable=True,
		neutrons=2,
		protons=2
	),
	# He-5 (unstable)
	Isotope(
		symbol="He-5",
		mass_number=5,
		atomic_mass=5.012057,
		half_life=7e-22,
		half_life_unit="s",
		decay_mode=DecayMode.NEUTRON_EMISSION,
		stable=False,
		neutrons=3,
		protons=2
	),
	# He-6 (unstable)
	Isotope(
		symbol="He-6",
		mass_number=6,
		atomic_mass=6.019222,
		half_life=0.807,
		half_life_unit="s",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=4,
		protons=2
	),
	# He-7 (unstable)
	Isotope(
		symbol="He-7",
		mass_number=7,
		atomic_mass=7.027992,
		half_life=2.9e-21,
		half_life_unit="s",
		decay_mode=DecayMode.NEUTRON_EMISSION,
		stable=False,
		neutrons=5,
		protons=2
	),
	# He-8 (unstable)
	Isotope(
		symbol="He-8",
		mass_number=8,
		atomic_mass=8.033922,
		half_life=0.119,
		half_life_unit="s",
		decay_mode=DecayMode.BETA_MINUS,
		stable=False,
		neutrons=6,
		protons=2
	),
	# He-9 (unstable)
	Isotope(
		symbol="He-9",
		mass_number=9,
		atomic_mass=9.043946,
		half_life=2.6e-21,
		half_life_unit="s",
		decay_mode=DecayMode.NEUTRON_EMISSION,
		stable=False,
		neutrons=7,
		protons=2
	),
	# He-10 (unstable)
	Isotope(
		symbol="He-10",
		mass_number=10,
		atomic_mass=10.052590,
		half_life=2.6e-21,
		half_life_unit="s",
		decay_mode=DecayMode.NEUTRON_EMISSION,
		stable=False,
		neutrons=8,
		protons=2
	),
]

# Helium element
Helium = Element(
	atomic_number=2,
	symbol="He",
	name="Helium",
	atomic_mass=4.0026,
	category=ElementCategory.NOBLE_GAS.value,
	phase=Phase.GAS.value,
	density=0.0001785,
	melting_point=0.95,
	boiling_point=4.22,
	electron_config="1s2",
	electronegativity=None,
	ionization_energy=24.587,
	electron_affinity=0,
	atomic_radius=31,
	covalent_radius=28,
	van_der_waals_radius=140,
	oxidation_states=[0],
	isotopes=HELIUM_ISOTOPES,
	discovered_by="Pierre Janssen",
	year_discovered=1868,
	description="Helium is a colorless, odorless, tasteless, non-toxic, inert, monatomic gas."
)

__all__ = ['Helium', 'HELIUM_ISOTOPES']
