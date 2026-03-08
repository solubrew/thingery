# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Oxygen Element
	description: >
		Oxygen element with all isotopes
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


# Oxygen (O) - Atomic Number 8
@dataclass
class Oxygen(Element):
    """Oxygen element with comprehensive isotope data"""
    
    def __init__(self):
        super().__init__(
            atomic_number=8,
            symbol="O",
            name="Oxygen",
            atomic_mass=15.999,
            category=ElementCategory.NONMETAL.value,
            phase=Phase.GAS.value,
            density=0.001429,
            melting_point=54.36,
            boiling_point=90.20,
            electron_config="[He] 2s2 2p4",
            electronegativity=3.44,
            ionization_energy=1313.9,
            isotopes=[
                # Stable isotopes
                Isotope(mass_number=16, symbol="O-16", atomic_mass=15.994915, abundance=99.757, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=17, symbol="O-17", atomic_mass=16.999132, abundance=0.038, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=18, symbol="O-18", atomic_mass=17.999160, abundance=0.205, decay_mode=DecayMode.STABLE.value),
                # Unstable isotopes
                Isotope(mass_number=12, symbol="O-12", atomic_mass=12.034405, half_life=1.1e-21, decay_mode=DecayMode.PROTON_EMISSION.value),
                Isotope(mass_number=13, symbol="O-13", atomic_mass=13.024812, half_life=8.58e-3, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=14, symbol="O-14", atomic_mass=14.008596, half_life=70.6, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=15, symbol="O-15", atomic_mass=15.003065, half_life=122.2, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=19, symbol="O-19", atomic_mass=19.003580, half_life=26.9, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=20, symbol="O-20", atomic_mass=20.004077, half_life=13.5, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=21, symbol="O-21", atomic_mass=21.008656, half_life=3.42, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=22, symbol="O-22", atomic_mass=22.00997, half_life=2.25, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=23, symbol="O-23", atomic_mass=23.01569, half_life=0.082, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=24, symbol="O-24", atomic_mass=24.02047, half_life=0.065, decay_mode=DecayMode.BETA_MINUS.value),
            ]
        )


# Oxygen Isotope - Oxygen-16
@dataclass
class Oxygen16(Isotope):
    """Oxygen-16 (most abundant)"""
    
    def __init__(self):
        super().__init__(
            mass_number=16,
            symbol="O-16",
            atomic_mass=15.994915,
            abundance=99.757,
            decay_mode=DecayMode.STABLE.value
        )


# Oxygen Isotope - Oxygen-17
@dataclass
class Oxygen17(Isotope):
    """Oxygen-17 (NMR active)"""
    
    def __init__(self):
        super().__init__(
            mass_number=17,
            symbol="O-17",
            atomic_mass=16.999132,
            abundance=0.038,
            decay_mode=DecayMode.STABLE.value
        )


# Oxygen Isotope - Oxygen-18
@dataclass
class Oxygen18(Isotope):
    """Oxygen-18 (heavy water component)"""
    
    def __init__(self):
        super().__init__(
            mass_number=18,
            symbol="O-18",
            atomic_mass=17.999160,
            abundance=0.205,
            decay_mode=DecayMode.STABLE.value
        )


# Export all
__all__ = ['Oxygen', 'Oxygen16', 'Oxygen17', 'Oxygen18']
