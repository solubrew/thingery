# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Uranium Element
	description: >
		Uranium element with all isotopes
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
class Uranium(Element):
    """Uranium element with comprehensive isotope data"""
    
    def __init__(self):
        super().__init__(
            atomic_number=92,
            symbol="U",
            name="Uranium",
            atomic_mass=238.029,
            category=ElementCategory.ACTINIDE.value,
            phase=Phase.SOLID.value,
            density=18.95,
            melting_point=1405.3,
            boiling_point=4404.0,
            electron_config="[Rn] 5f3 6d1 7s2",
            electronegativity=1.38,
            ionization_energy=597.6,
            isotopes=[
                Isotope(mass_number=217, symbol="U-217", atomic_mass=217.02466, half_life=1.2e-3, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=218, symbol="U-218", atomic_mass=218.02350, half_life=1.5e-3, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=219, symbol="U-219", atomic_mass=219.02496, half_life=0.042, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=227, symbol="U-227", atomic_mass=227.02884, half_life=1.1, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=228, symbol="U-228", atomic_mass=228.03074, half_life=9.1, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=229, symbol="U-229", atomic_mass=229.033506, half_life=58.0, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=230, symbol="U-230", atomic_mass=230.03394, half_life=20.8, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=231, symbol="U-231", atomic_mass=231.03629, half_life=4.2, decay_mode=DecayMode.BETA_PLUS.value),
                Isotope(mass_number=232, symbol="U-232", atomic_mass=232.037156, half_life=68.9, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=233, symbol="U-233", atomic_mass=233.039635, half_life=1.592e5, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=234, symbol="U-234", atomic_mass=234.040952, abundance=0.0054, half_life=2.455e5, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=235, symbol="U-235", atomic_mass=235.043930, abundance=0.7204, half_life=7.038e8, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=236, symbol="U-236", atomic_mass=236.045568, half_life=2.342e7, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=237, symbol="U-237", atomic_mass=237.048730, half_life=6.75, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=238, symbol="U-238", atomic_mass=238.050788, abundance=99.2742, half_life=4.468e9, decay_mode=DecayMode.ALPHA.value),
                Isotope(mass_number=239, symbol="U-239", atomic_mass=239.054293, half_life=23.45, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=240, symbol="U-240", atomic_mass=240.05659, half_life=14.1, decay_mode=DecayMode.BETA_MINUS.value),
            ]
        )


@dataclass
class Uranium234(Isotope):
    """Uranium-234 (U-234)"""
    
    def __init__(self):
        super().__init__(
            mass_number=234,
            symbol="U-234",
            atomic_mass=234.040952,
            abundance=0.0054,
            half_life=2.455e5,
            decay_mode=DecayMode.ALPHA.value
        )


@dataclass
class Uranium235(Isotope):
    """Uranium-235 ( fissile)"""
    
    def __init__(self):
        super().__init__(
            mass_number=235,
            symbol="U-235",
            atomic_mass=235.043930,
            abundance=0.7204,
            half_life=7.038e8,
            decay_mode=DecayMode.ALPHA.value
        )


@dataclass
class Uranium238(Isotope):
    """Uranium-238 (most abundant, parent of uranium series)"""
    
    def __init__(self):
        super().__init__(
            mass_number=238,
            symbol="U-238",
            atomic_mass=238.050788,
            abundance=99.2742,
            half_life=4.468e9,
            decay_mode=DecayMode.ALPHA.value
        )


__all__ = ['Uranium', 'Uranium234', 'Uranium235', 'Uranium238']
