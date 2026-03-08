# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Lithium Element
	description: >
		Lithium element with all isotopes
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
class Lithium(Element):
    """Lithium element with comprehensive isotope data"""
    
    def __init__(self):
        super().__init__(
            atomic_number=3,
            symbol="Li",
            name="Lithium",
            atomic_mass=6.94,
            category=ElementCategory.ALKALI_METAL.value,
            phase=Phase.SOLID.value,
            density=0.534,
            melting_point=453.69,
            boiling_point=1560.0,
            electron_config="[He] 2s1",
            electronegativity=0.98,
            ionization_energy=520.2,
            isotopes=[
                Isotope(mass_number=3, symbol="Li-3", atomic_mass=3.030786, half_life=4.0e-21, decay_mode=DecayMode.PROTON_EMISSION.value),
                Isotope(mass_number=4, symbol="Li-4", atomic_mass=4.027186, half_life=9.1e-23, decay_mode=DecayMode.PROTON_EMISSION.value),
                Isotope(mass_number=5, symbol="Li-5", atomic_mass=5.012537, half_life=3.0e-21, decay_mode=DecayMode.PROTON_EMISSION.value),
                Isotope(mass_number=6, symbol="Li-6", atomic_mass=6.015122, abundance=7.59, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=7, symbol="Li-7", atomic_mass=7.016004, abundance=92.41, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=8, symbol="Li-8", atomic_mass=8.022486, half_life=0.838, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=9, symbol="Li-9", atomic_mass=9.026790, half_life=0.178, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=10, symbol="Li-10", atomic_mass=10.035481, half_life=3.7e-21, decay_mode=DecayMode.NEUTRON_EMISSION.value),
                Isotope(mass_number=11, symbol="Li-11", atomic_mass=11.043798, half_life=0.00875, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=12, symbol="Li-12", atomic_mass=12.05378, half_life=1.0e-21, decay_mode=DecayMode.NEUTRON_EMISSION.value),
            ]
        )


@dataclass
class Lithium6(Isotope):
    """Lithium-6 (nuclear applications)"""
    
    def __init__(self):
        super().__init__(
            mass_number=6,
            symbol="Li-6",
            atomic_mass=6.015122,
            abundance=7.59,
            decay_mode=DecayMode.STABLE.value
        )


@dataclass
class Lithium7(Isotope):
    """Lithium-7 (most abundant)"""
    
    def __init__(self):
        super().__init__(
            mass_number=7,
            symbol="Li-7",
            atomic_mass=7.016004,
            abundance=92.41,
            decay_mode=DecayMode.STABLE.value
        )


__all__ = ['Lithium', 'Lithium6', 'Lithium7']
