# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Iron Element
	description: >
		Iron element with all isotopes
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from dataclasses import dataclass

from thingery.models import Element, Isotope, ElementCategory, Phase, DecayMode


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


@dataclass
class Iron(Element):
    """Iron element with comprehensive isotope data"""
    
    def __init__(self):
        super().__init__(
            atomic_number=26,
            symbol="Fe",
            name="Iron",
            atomic_mass=55.845,
            category=ElementCategory.TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=7.874,
            melting_point=1811.0,
            boiling_point=3134.0,
            electron_config="[Ar] 3d6 4s2",
            electronegativity=1.83,
            ionization_energy=762.5,
            isotopes=[
                Isotope(mass_number=45, symbol="Fe-45", atomic_mass=44.962888, half_life=1.9e-21, decay_mode=DecayMode.PROTON_EMISSION.value),
                Isotope(mass_number=46, symbol="Fe-46", atomic_mass=45.954581, half_life=9.0e-21, decay_mode=DecayMode.PROTON_EMISSION.value),
                Isotope(mass_number=47, symbol="Fe-47", atomic_mass=46.950764, half_life=3.9e-21, decay_mode=DecayMode.PROTON_EMISSION.value),
                Isotope(mass_number=48, symbol="Fe-48", atomic_mass=47.948936, half_life=0.044, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=49, symbol="Fe-49", atomic_mass=48.946610, half_life=0.065, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=50, symbol="Fe-50", atomic_mass=49.944988, half_life=0.145, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=51, symbol="Fe-51", atomic_mass=50.943705, half_life=8.27, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=52, symbol="Fe-52", atomic_mass=51.942114, half_life=8.275, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=53, symbol="Fe-53", atomic_mass=52.945308, half_life=8.51, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=54, symbol="Fe-54", atomic_mass=53.939610, abundance=5.845, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=55, symbol="Fe-55", atomic_mass=54.938293, half_life=2.73, decay_mode=DecayMode.ELECTRON_CAPTURE.value),
                Isotope(mass_number=56, symbol="Fe-56", atomic_mass=55.934937, abundance=91.754, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=57, symbol="Fe-57", atomic_mass=56.935394, abundance=2.119, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=58, symbol="Fe-58", atomic_mass=57.933276, abundance=0.282, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=59, symbol="Fe-59", atomic_mass=58.934875, half_life=44.495, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=60, symbol="Fe-60", atomic_mass=59.934072, half_life=2.6e6, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=61, symbol="Fe-61", atomic_mass=60.936745, half_life=0.196, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=62, symbol="Fe-62", atomic_mass=61.936767, half_life=0.068, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=63, symbol="Fe-63", atomic_mass=62.94037, half_life=0.0061, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=64, symbol="Fe-64", atomic_mass=63.94109, half_life=0.002, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=65, symbol="Fe-65", atomic_mass=64.94538, half_life=0.0013, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=66, symbol="Fe-66", atomic_mass=65.94626, half_life=0.0015, decay_mode=DecayMode.BETA_MINUS.value),
            ]
        )


@dataclass
class Iron54(Isotope):
    """Iron-54"""
    
    def __init__(self):
        super().__init__(
            mass_number=54,
            symbol="Fe-54",
            atomic_mass=53.939610,
            abundance=5.845,
            decay_mode=DecayMode.STABLE.value
        )


@dataclass
class Iron56(Isotope):
    """Iron-56 (most abundant, used in steel)"""
    
    def __init__(self):
        super().__init__(
            mass_number=56,
            symbol="Fe-56",
            atomic_mass=55.934937,
            abundance=91.754,
            decay_mode=DecayMode.STABLE.value
        )


@dataclass
class Iron57(Isotope):
    """Iron-57 (Mössbauer spectroscopy)"""
    
    def __init__(self):
        super().__init__(
            mass_number=57,
            symbol="Fe-57",
            atomic_mass=56.935394,
            abundance=2.119,
            decay_mode=DecayMode.STABLE.value
        )


@dataclass
class Iron60(Isotope):
    """Iron-60 (cosmic ray chronometer)"""
    
    def __init__(self):
        super().__init__(
            mass_number=60,
            symbol="Fe-60",
            atomic_mass=59.934072,
            half_life=2.6e6,
            decay_mode=DecayMode.BETA_MINUS.value
        )


__all__ = ['Iron', 'Iron54', 'Iron56', 'Iron57', 'Iron60']
