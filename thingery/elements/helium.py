# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Helium Element
	description: >
		Helium element with all isotopes
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


# Helium (He) - Atomic Number 2
@dataclass
class Helium(Element):
    """Helium element with comprehensive isotope data"""
    
    def __init__(self):
        super().__init__(
            atomic_number=2,
            symbol="He",
            name="Helium",
            atomic_mass=4.003,
            category=ElementCategory.NOBLE_GAS.value,
            phase=Phase.GAS.value,
            density=0.0001785,
            melting_point=0.95,
            boiling_point=4.22,
            electron_config="1s2",
            electronegativity=None,
            ionization_energy=2372.3,
            isotopes=[
                # Stable isotopes
                Isotope(mass_number=3, symbol="He", atomic_mass=3.016029, abundance=0.000137, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=4, symbol="He", atomic_mass=4.002603, abundance=99.999863, decay_mode=DecayMode.STABLE.value),
                # Unstable isotopes
                Isotope(mass_number=2, symbol="He-2", atomic_mass=2.015127, half_life=1.0e-21, decay_mode=DecayMode.PROTON_EMISSION.value),
                Isotope(mass_number=5, symbol="He-5", atomic_mass=5.012057, half_life=7.6e-23, decay_mode=DecayMode.NEUTRON_EMISSION.value),
                Isotope(mass_number=6, symbol="He-6", atomic_mass=6.019886, half_life=0.807, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=7, symbol="He-7", atomic_mass=7.027992, half_life=2.9e-21, decay_mode=DecayMode.NEUTRON_EMISSION.value),
                Isotope(mass_number=8, symbol="He-8", atomic_mass=8.033934, half_life=0.119, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=9, symbol="He-9", atomic_mass=9.043946, half_life=2.6e-21, decay_mode=DecayMode.NEUTRON_EMISSION.value),
                Isotope(mass_number=10, symbol="He-10", atomic_mass=10.052791, half_life=2.6e-23, decay_mode=DecayMode.NEUTRON_EMISSION.value),
            ]
        )


# Helium Isotope - Helium-3
@dataclass
class Helium3(Isotope):
    """Helium-3"""
    
    def __init__(self):
        super().__init__(
            mass_number=3,
            symbol="He-3",
            atomic_mass=3.016029,
            abundance=0.000137,
            decay_mode=DecayMode.STABLE.value
        )


# Helium Isotope - Helium-4
@dataclass
class Helium4(Isotope):
    """Helium-4 (Alpha particle)"""
    
    def __init__(self):
        super().__init__(
            mass_number=4,
            symbol="He-4",
            atomic_mass=4.002603,
            abundance=99.999863,
            decay_mode=DecayMode.STABLE.value
        )


# Export all
__all__ = ['Helium', 'Helium3', 'Helium4']
