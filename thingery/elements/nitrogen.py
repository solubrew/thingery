# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Nitrogen Element
	description: >
		Nitrogen element with all isotopes
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


# Nitrogen (N) - Atomic Number 7
@dataclass
class Nitrogen(Element):
    """Nitrogen element with comprehensive isotope data"""
    
    def __init__(self):
        super().__init__(
            atomic_number=7,
            symbol="N",
            name="Nitrogen",
            atomic_mass=14.007,
            category=ElementCategory.NONMETAL.value,
            phase=Phase.GAS.value,
            density=0.0012506,
            melting_point=63.15,
            boiling_point=77.36,
            electron_config="[He] 2s2 2p3",
            electronegativity=3.04,
            ionization_energy=1402.3,
            isotopes=[
                # Stable isotopes
                Isotope(mass_number=14, symbol="N-14", atomic_mass=14.003074, abundance=99.632, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=15, symbol="N-15", atomic_mass=15.000109, abundance=0.368, decay_mode=DecayMode.STABLE.value),
                # Unstable isotopes
                Isotope(mass_number=10, symbol="N-10", atomic_mass=10.012536, half_life=2.6e-21, decay_mode=DecayMode.PROTON_EMISSION.value),
                Isotope(mass_number=11, symbol="N-11", atomic_mass=11.026091, half_life=0.59, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=12, symbol="N-12", atomic_mass=12.018613, half_life=11.0, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=13, symbol="N-13", atomic_mass=13.009354, half_life=9.97, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=16, symbol="N-16", atomic_mass=16.006101, half_life=7.13, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=17, symbol="N-17", atomic_mass=17.014679, half_life=4.17, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=18, symbol="N-18", atomic_mass=18.020079, half_life=0.624, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=19, symbol="N-19", atomic_mass=19.027029, half_life=0.271, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=20, symbol="N-20", atomic_mass=20.03237, half_life=0.097, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=21, symbol="N-21", atomic_mass=21.04111, half_life=0.085, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=22, symbol="N-22", atomic_mass=22.05039, half_life=0.018, decay_mode=DecayMode.BETA_MINUS.value),
            ]
        )


# Nitrogen Isotope - Nitrogen-14
@dataclass
class Nitrogen14(Isotope):
    """Nitrogen-14"""
    
    def __init__(self):
        super().__init__(
            mass_number=14,
            symbol="N-14",
            atomic_mass=14.003074,
            abundance=99.632,
            decay_mode=DecayMode.STABLE.value
        )


# Nitrogen Isotope - Nitrogen-15
@dataclass
class Nitrogen15(Isotope):
    """Nitrogen-15 (NMR active)"""
    
    def __init__(self):
        super().__init__(
            mass_number=15,
            symbol="N-15",
            atomic_mass=15.000109,
            abundance=0.368,
            decay_mode=DecayMode.STABLE.value
        )


# Export all
__all__ = ['Nitrogen', 'Nitrogen14', 'Nitrogen15']
