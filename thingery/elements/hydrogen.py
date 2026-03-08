# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Hydrogen Element
	description: >
		Hydrogen element with all isotopes
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


# Hydrogen (H) - Atomic Number 1
@dataclass
class Hydrogen(Element):
    """Hydrogen element with comprehensive isotope data"""
    
    def __init__(self):
        super().__init__(
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
            ionization_energy=1312.0,
            isotopes=[
                # Stable isotopes
                Isotope(mass_number=1, symbol="H", atomic_mass=1.007825, abundance=99.9844, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=2, symbol="D", atomic_mass=2.014102, abundance=0.0156, decay_mode=DecayMode.STABLE.value),
                # Unstable isotopes
                Isotope(mass_number=3, symbol="T", atomic_mass=3.016049, half_life=12.32, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=4, symbol="H-4", atomic_mass=4.027812, half_life=1.39e-22, decay_mode=DecayMode.NEUTRON_EMISSION.value),
                Isotope(mass_number=5, symbol="H-5", atomic_mass=5.035311, half_life=8.6e-23, decay_mode=DecayMode.NEUTRON_EMISSION.value),
                Isotope(mass_number=6, symbol="H-6", atomic_mass=6.044944, half_life=3.3e-27, decay_mode=DecayMode.NEUTRON_EMISSION.value),
                Isotope(mass_number=7, symbol="H-7", atomic_mass=7.053766, half_life=2.3e-27, decay_mode=DecayMode.NEUTRON_EMISSION.value),
            ]
        )


# Hydrogen Isotope - Deuterium
@dataclass
class Deuterium(Isotope):
    """Deuterium (D) - Hydrogen-2"""
    
    def __init__(self):
        super().__init__(
            mass_number=2,
            symbol="D",
            atomic_mass=2.014102,
            abundance=0.0156,
            decay_mode=DecayMode.STABLE.value
        )


# Hydrogen Isotope - Tritium
@dataclass
class Tritium(Isotope):
    """Tritium (T) - Hydrogen-3"""
    
    def __init__(self):
        super().__init__(
            mass_number=3,
            symbol="T",
            atomic_mass=3.016049,
            half_life=12.32,
            decay_mode=DecayMode.BETA_MINUS.value
        )


# Export all
__all__ = ['Hydrogen', 'Deuterium', 'Tritium']
