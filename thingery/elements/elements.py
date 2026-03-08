# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Elements
	description: >
		Complete element database with isotopes
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from dataclasses import dataclass, field
from typing import List, Optional
from thingery.models import Element, Isotope, ElementCategory, Phase, DecayMode


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


# Hydrogen (H) - Atomic Number 1
@dataclass
class Hydrogen(Element):
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
                Isotope(mass_number=1, symbol="H", atomic_mass=1.007825, abundance=99.9844, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=2, symbol="D", atomic_mass=2.014102, abundance=0.0156, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=3, symbol="T", atomic_mass=3.016049, half_life=12.32, decay_mode=DecayMode.BETA_MINUS.value),
            ]
        )


# Helium (He) - Atomic Number 2
@dataclass
class Helium(Element):
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
                Isotope(mass_number=3, symbol="He", atomic_mass=3.016029, abundance=0.000137, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=4, symbol="He", atomic_mass=4.002603, abundance=99.999863, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Lithium (Li) - Atomic Number 3
@dataclass
class Lithium(Element):
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
                Isotope(mass_number=6, symbol="Li", atomic_mass=6.015122, abundance=7.59, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=7, symbol="Li", atomic_mass=7.016004, abundance=92.41, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Beryllium (Be) - Atomic Number 4
@dataclass
class Beryllium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=4,
            symbol="Be",
            name="Beryllium",
            atomic_mass=9.012,
            category=ElementCategory.ALKALINE_EARTH_METAL.value,
            phase=Phase.SOLID.value,
            density=1.85,
            melting_point=1560.0,
            boiling_point=2742.0,
            electron_config="[He] 2s2",
            electronegativity=1.57,
            ionization_energy=899.5,
            isotopes=[
                Isotope(mass_number=9, symbol="Be", atomic_mass=9.012182, abundance=100.0, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Boron (B) - Atomic Number 5
@dataclass
class Boron(Element):
    def __init__(self):
        super().__init__(
            atomic_number=5,
            symbol="B",
            name="Boron",
            atomic_mass=10.81,
            category=ElementCategory.METALLOID.value,
            phase=Phase.SOLID.value,
            density=2.34,
            melting_point=2349.0,
            boiling_point=4200.0,
            electron_config="[He] 2s2 2p1",
            electronegativity=2.04,
            ionization_energy=800.6,
            isotopes=[
                Isotope(mount_number=10, symbol="B", atomic_mass=10.012937, abundance=19.9, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=11, symbol="B", atomic_mass=11.009305, abundance=80.1, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Carbon (C) - Atomic Number 6
@dataclass
class Carbon(Element):
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
                Isotope(mass_number=12, symbol="C", atomic_mass=12.0, abundance=98.93, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=13, symbol="C", atomic_mass=13.003355, abundance=1.07, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=14, symbol="C", atomic_mass=14.003242, half_life=5730.0, decay_mode=DecayMode.BETA_MINUS.value),
            ]
        )


# Nitrogen (N) - Atomic Number 7
@dataclass
class Nitrogen(Element):
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
                Isotope(mass_number=14, symbol="N", atomic_mass=14.003074, abundance=99.632, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=15, symbol="N", atomic_mass=15.000109, abundance=0.368, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Oxygen (O) - Atomic Number 8
@dataclass
class Oxygen(Element):
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
                Isotope(mass_number=16, symbol="O", atomic_mass=15.994915, abundance=99.757, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=17, symbol="O", atomic_mass=16.999132, abundance=0.038, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=18, symbol="O", atomic_mass=17.999160, abundance=0.205, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Fluorine (F) - Atomic Number 9
@dataclass
class Fluorine(Element):
    def __init__(self):
        super().__init__(
            atomic_number=9,
            symbol="F",
            name="Fluorine",
            atomic_mass=18.998,
            category=ElementCategory.HALOGEN.value,
            phase=Phase.GAS.value,
            density=0.001696,
            melting_point=53.53,
            boiling_point=85.03,
            electron_config="[He] 2s2 2p5",
            electronegativity=3.98,
            ionization_energy=1681.0,
            isotopes=[
                Isotope(mass_number=19, symbol="F", atomic_mass=18.998403, abundance=100.0, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Neon (Ne) - Atomic Number 10
@dataclass
class Neon(Element):
    def __init__(self):
        super().__init__(
            atomic_number=10,
            symbol="Ne",
            name="Neon",
            atomic_mass=20.180,
            category=ElementCategory.NOBLE_GAS.value,
            phase=Phase.GAS.value,
            density=0.0008999,
            melting_point=24.56,
            boiling_point=27.07,
            electron_config="[He] 2s2 2p6",
            electronegativity=None,
            ionization_energy=2080.7,
            isotopes=[
                Isotope(mass_number=20, symbol="Ne", atomic_mass=19.992440, abundance=90.48, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=21, symbol="Ne", atomic_mass=20.993847, abundance=0.27, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=22, symbol="Ne", atomic_mass=21.991386, abundance=9.25, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Sodium (Na) - Atomic Number 11
@dataclass
class Sodium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=11,
            symbol="Na",
            name="Sodium",
            atomic_mass=22.990,
            category=ElementCategory.ALKALI_METAL.value,
            phase=Phase.SOLID.value,
            density=0.971,
            melting_point=370.87,
            boiling_point=1156.0,
            electron_config="[Ne] 3s1",
            electronegativity=0.93,
            ionization_energy=495.8,
            isotopes=[
                Isotope(mass_number=23, symbol="Na", atomic_mass=22.989770, abundance=100.0, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Magnesium (Mg) - Atomic Number 12
@dataclass
class Magnesium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=12,
            symbol="Mg",
            name="Magnesium",
            atomic_mass=24.305,
            category=ElementCategory.ALKALINE_EARTH_METAL.value,
            phase=Phase.SOLID.value,
            density=1.738,
            melting_point=923.0,
            boiling_point=1363.0,
            electron_config="[Ne] 3s2",
            electronegativity=1.31,
            ionization_energy=737.7,
            isotopes=[
                Isotope(mass_number=24, symbol="Mg", atomic_mass=23.985042, abundance=78.99, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=25, symbol="Mg", atomic_mass=24.985837, abundance=10.00, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=26, symbol="Mg", atomic_mass=25.982593, abundance=11.01, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Aluminum (Al) - Atomic Number 13
@dataclass
class Aluminum(Element):
    def __init__(self):
        super().__init__(
            atomic_number=13,
            symbol="Al",
            name="Aluminum",
            atomic_mass=26.982,
            category=ElementCategory.POST_TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=2.698,
            melting_point=933.47,
            boiling_point=2792.0,
            electron_config="[Ne] 3s2 3p1",
            electronegativity=1.61,
            ionization_energy=577.5,
            isotopes=[
                Isotope(mass_number=27, symbol="Al", atomic_mass=26.981539, abundance=100.0, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Silicon (Si) - Atomic Number 14
@dataclass
class Silicon(Element):
    def __init__(self):
        super().__init__(
            atomic_number=14,
            symbol="Si",
            name="Silicon",
            atomic_mass=28.086,
            category=ElementCategory.METALLOID.value,
            phase=Phase.SOLID.value,
            density=2.3296,
            melting_point=1687.0,
            boiling_point=3538.0,
            electron_config="[Ne] 3s2 3p2",
            electronegativity=1.90,
            ionization_energy=786.5,
            isotopes=[
                Isotope(mass_number=28, symbol="Si", atomic_mass=27.976927, abundance=92.23, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=29, symbol="Si", atomic_mass=28.976495, abundance=4.68, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=30, symbol="Si", atomic_mass=29.973770, abundance=3.09, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Phosphorus (P) - Atomic Number 15
@dataclass
class Phosphorus(Element):
    def __init__(self):
        super().__init__(
            atomic_number=15,
            symbol="P",
            name="Phosphorus",
            atomic_mass=30.974,
            category=ElementCategory.NONMETAL.value,
            phase=Phase.SOLID.value,
            density=1.82,
            melting_point=317.30,
            boiling_point=550.0,
            electron_config="[Ne] 3s2 3p3",
            electronegativity=2.19,
            ionization_energy=1011.8,
            isotopes=[
                Isotope(mass_number=31, symbol="P", atomic_mass=30.973762, abundance=100.0, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Sulfur (S) - Atomic Number 16
@dataclass
class Sulfur(Element):
    def __init__(self):
        super().__init__(
            atomic_number=16,
            symbol="S",
            name="Sulfur",
            atomic_mass=32.065,
            category=ElementCategory.NONMETAL.value,
            phase=Phase.SOLID.value,
            density=2.067,
            melting_point=388.36,
            boiling_point=717.87,
            electron_config="[Ne] 3s2 3p4",
            electronegativity=2.58,
            ionization_energy=999.6,
            isotopes=[
                Isotope(mass_number=32, symbol="S", atomic_mass=31.972071, abundance=94.93, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=33, symbol="S", atomic_mass=32.971458, abundance=0.76, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=34, symbol="S", atomic_mass=33.967867, abundance=4.29, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=36, symbol="S", atomic_mass=35.967081, abundance=0.02, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Chlorine (Cl) - Atomic Number 17
@dataclass
class Chlorine(Element):
    def __init__(self):
        super().__init__(
            atomic_number=17,
            symbol="Cl",
            name="Chlorine",
            atomic_mass=35.453,
            category=ElementCategory.HALOGEN.value,
            phase=Phase.GAS.value,
            density=0.003214,
            melting_point=171.6,
            boiling_point=239.11,
            electron_config="[Ne] 3s2 3p5",
            electronegativity=3.16,
            ionization_energy=1251.2,
            isotopes=[
                Isotope(mass_number=35, symbol="Cl", atomic_mass=34.968853, abundance=75.76, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=37, symbol="Cl", atomic_mass=36.965903, abundance=24.24, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Argon (Ar) - Atomic Number 18
@dataclass
class Argon(Element):
    def __init__(self):
        super().__init__(
            atomic_number=18,
            symbol="Ar",
            name="Argon",
            atomic_mass=39.948,
            category=ElementCategory.NOBLE_GAS.value,
            phase=Phase.GAS.value,
            density=0.0017837,
            melting_point=83.80,
            boiling_point=87.30,
            electron_config="[Ne] 3s2 3p6",
            electronegativity=None,
            ionization_energy=1520.6,
            isotopes=[
                Isotope(mass_number=36, symbol="Ar", atomic_mass=35.967545, abundance=0.334, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=38, symbol="Ar", atomic_mass=37.962732, abundance=0.063, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=40, symbol="Ar", atomic_mass=39.962383, abundance=99.603, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Potassium (K) - Atomic Number 19
@dataclass
class Potassium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=19,
            symbol="K",
            name="Potassium",
            atomic_mass=39.098,
            category=ElementCategory.ALKALI_METAL.value,
            phase=Phase.SOLID.value,
            density=0.862,
            melting_point=336.53,
            boiling_point=1032.0,
            electron_config="[Ar] 4s1",
            electronegativity=0.82,
            ionization_energy=418.8,
            isotopes=[
                Isotope(mass_number=39, symbol="K", atomic_mass=38.963707, abundance=93.2581, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=40, symbol="K", atomic_mass=39.963998, half_life=1.248e9, decay_mode=DecayMode.BETA_MINUS.value),
                Isotope(mass_number=41, symbol="K", atomic_mass=40.961826, abundance=6.7302, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Calcium (Ca) - Atomic Number 20
@dataclass
class Calcium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=20,
            symbol="Ca",
            name="Calcium",
            atomic_mass=40.078,
            category=ElementCategory.ALKALINE_EARTH_METAL.value,
            phase=Phase.SOLID.value,
            density=1.54,
            melting_point=1115.0,
            boiling_point=1757.0,
            electron_config="[Ar] 4s2",
            electronegativity=1.00,
            ionization_energy=589.8,
            isotopes=[
                Isotope(mass_number=40, symbol="Ca", atomic_mass=39.962591, abundance=96.941, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=42, symbol="Ca", atomic_mass=41.958618, abundance=0.647, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=44, symbol="Ca", atomic_mass=43.955481, abundance=2.086, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=48, symbol="Ca", atomic_mass=47.952534, abundance=0.187, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Iron (Fe) - Atomic Number 26
@dataclass
class Iron(Element):
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
                Isotope(mass_number=54, symbol="Fe", atomic_mass=53.939610, abundance=5.845, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=56, symbol="Fe", atomic_mass=55.934937, abundance=91.754, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=57, symbol="Fe", atomic_mass=56.935394, abundance=2.119, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=58, symbol="Fe", atomic_mass=57.933276, abundance=0.282, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Copper (Cu) - Atomic Number 29
@dataclass
class Copper(Element):
    def __init__(self):
        super().__init__(
            atomic_number=29,
            symbol="Cu",
            name="Copper",
            atomic_mass=63.546,
            category=ElementCategory.TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=8.96,
            melting_point=1357.77,
            boiling_point=2835.0,
            electron_config="[Ar] 3d10 4s1",
            electronegativity=1.90,
            ionization_energy=745.5,
            isotopes=[
                Isotope(mass_number=63, symbol="Cu", atomic_mass=62.929601, abundance=69.17, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=65, symbol="Cu", atomic_mass=64.927789, abundance=30.83, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Silver (Ag) - Atomic Number 47
@dataclass
class Silver(Element):
    def __init__(self):
        super().__init__(
            atomic_number=47,
            symbol="Ag",
            name="Silver",
            atomic_mass=107.868,
            category=ElementCategory.TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=10.501,
            melting_point=1234.93,
            boiling_point=2435.0,
            electron_config="[Kr] 4d10 5s1",
            electronegativity=1.93,
            ionization_energy=731.0,
            isotopes=[
                Isotope(mass_number=107, symbol="Ag", atomic_mass=106.905097, abundance=51.839, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=109, symbol="Ag", atomic_mass=108.904752, abundance=48.161, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Gold (Au) - Atomic Number 79
@dataclass
class Gold(Element):
    def __init__(self):
        super().__init__(
            atomic_number=79,
            symbol="Au",
            name="Gold",
            atomic_mass=196.967,
            category=ElementCategory.TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=19.282,
            melting_point=1337.33,
            boiling_point=3129.0,
            electron_config="[Xe] 4f14 5d10 6s1",
            electronegativity=2.54,
            ionization_energy=890.1,
            isotopes=[
                Isotope(mass_number=197, symbol="Au", atomic_mass=196.966552, abundance=100.0, decay_mode=DecayMode.STABLE.value),
            ]
        )


# All elements export
__all__ = [
    'Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen',
    'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus',
    'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium',
    'Iron', 'Copper', 'Silver', 'Gold',
]
