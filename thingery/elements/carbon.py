# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Carbon Element
	description: >
		Carbon element with all isotopes
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from dataclasses import dataclass
from typing import List, Optional

from thingery.models import Element, Isotope, ElementCategory, Phase, DecayMode


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


# Carbon (C) - Atomic Number 6
@dataclass
class Carbon(Element):
    """Carbon element with comprehensive isotope data"""
    
    def __init__(self):
        super().__init__(
            atomic_number=6,
            symbol="C",
            name="Carbon",
            atomic_mass=12.011,
            category=ElementCategory.NONMETAL.value,
            phase=Phase.SOLID.value,
            density=2.267,
            melting_point=3823.0,
            boiling_point=4098.0,
            electron_config="[He] 2s2 2p2",
            electronegativity=2.55,
            ionization_energy=1086.5,
            isotopes=[
                # Stable isotopes
                Isotope(mass_number=12, symbol="C-12", atomic_mass=12.0, abundance=98.93, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=13, symbol="C-13", atomic_mass=13.003355, abundance=1.07, decay_mode=DecayMode.STABLE.value),
                # Unstable isotopes
                Isotope(mass_number=8, symbol="C-8", atomic_mass=8.037675, half_life=2.0e-21, decay_mode=DecayMode.PROTON_EMISSION.value),
                Isotope(mass_number=9, symbol="C-9", atomic_mass=9.031037, half_life=0.1265, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=10, symbol="C-10", atomic_mass=10.016853, half_life=19.3, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=11, symbol="C-11", atomic_mass=11.011434, half_life=20.4, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=14, symbol="C-14", atomic_mass=14.003242, half_life=5730.0, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=15, symbol="C-15", atomic_mass=15.010599, half_life=2.45, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=16, symbol="C-16", atomic_mass=16.014679, half_life=0.747, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=17, symbol="C-17", atomic_mass=17.022586, half_life=0.193, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=18, symbol="C-18", atomic_mass=18.02676, half_life=0.092, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=19, symbol="C-19", atomic_mass=19.03481, half_life=0.049, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=20, symbol="C-20", atomic_mass=20.04026, half_life=0.014, decay_mode=DecayMode.BETA_MINUS.value),
            ]
        )


# Carbon Isotope - Carbon-12
@dataclass
class Carbon12(Isotope):
    """Carbon-12 (defines atomic mass unit)"""
    
    def __init__(self):
        super().__init__(
            mass_number=12,
            symbol="C-12",
            atomic_mass=12.0,
            abundance=98.93,
            decay_mode=DecayMode.STABLE.value
        )


# Carbon Isotope - Carbon-13
@dataclass
class Carbon13(Isotope):
    """Carbon-13 (NMR active)"""
    
    def __init__(self):
        super().__init__(
            mass_number=13,
            symbol="C-13",
            atomic_mass=13.003355,
            abundance=1.07,
            decay_mode=DecayMode.STABLE.value
        )


# Carbon Isotope - Carbon-14
@dataclass
class Carbon14(Isotope):
    """Carbon-14 (radiocarbon dating)"""
    
    def __init__(self):
        super().__init__(
            mass_number=14,
            symbol="C-14",
            atomic_mass=14.003242,
            half_life=5730.0,
            decay_mode=DecayMode.BETA_MINUS.value
        )


# Export all
__all__ = ['Carbon', 'Carbon12', 'Carbon13', 'Carbon14']
