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


# Cobalt (Co) - Atomic Number 27
@dataclass
class Cobalt(Element):
    def __init__(self):
        super().__init__(
            atomic_number=27,
            symbol="Co",
            name="Cobalt",
            atomic_mass=58.933,
            category=ElementCategory.TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=8.86,
            melting_point=1768.0,
            boiling_point=3200.0,
            electron_config="[Ar] 3d7 4s2",
            electronegativity=1.88,
            ionization_energy=760.4,
            isotopes=[
                Isotope(mass_number=59, symbol="Co", atomic_mass=58.933195, abundance=100.0, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Nickel (Ni) - Atomic Number 28
@dataclass
class Nickel(Element):
    def __init__(self):
        super().__init__(
            atomic_number=28,
            symbol="Ni",
            name="Nickel",
            atomic_mass=58.693,
            category=ElementCategory.TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=8.912,
            melting_point=1728.0,
            boiling_point=3186.0,
            electron_config="[Ar] 3d8 4s2",
            electronegativity=1.91,
            ionization_energy=737.1,
            isotopes=[
                Isotope(mass_number=58, symbol="Ni", atomic_mass=57.935343, abundance=68.077, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=60, symbol="Ni", atomic_mass=59.930786, abundance=26.223, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=61, symbol="Ni", atomic_mass=60.931056, abundance=1.140, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=62, symbol="Ni", atomic_mass=61.928345, abundance=3.635, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=64, symbol="Ni", atomic_mass=63.927966, abundance=0.926, decay_mode=DecayMode.STABLE.value),
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


# Zinc (Zn) - Atomic Number 30
@dataclass
class Zinc(Element):
    def __init__(self):
        super().__init__(
            atomic_number=30,
            symbol="Zn",
            name="Zinc",
            atomic_mass=65.38,
            category=ElementCategory.TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=7.134,
            melting_point=692.88,
            boiling_point=1180.0,
            electron_config="[Ar] 3d10 4s2",
            electronegativity=1.65,
            ionization_energy=906.4,
            isotopes=[
                Isotope(mass_number=64, symbol="Zn", atomic_mass=63.929142, abundance=49.17, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=66, symbol="Zn", atomic_mass=65.926034, abundance=27.73, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=67, symbol="Zn", atomic_mass=66.927128, abundance=4.04, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=68, symbol="Zn", atomic_mass=67.924844, abundance=18.45, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=70, symbol="Zn", atomic_mass=69.925319, abundance=0.61, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Gallium (Ga) - Atomic Number 31
@dataclass
class Gallium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=31,
            symbol="Ga",
            name="Gallium",
            atomic_mass=69.723,
            category=ElementCategory.POST_TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=5.907,
            melting_point=302.91,
            boiling_point=2673.0,
            electron_config="[Ar] 3d10 4s2 4p1",
            electronegativity=1.81,
            ionization_energy=578.8,
            isotopes=[
                Isotope(mass_number=69, symbol="Ga", atomic_mass=68.925574, abundance=60.108, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=71, symbol="Ga", atomic_mass=70.924707, abundance=39.892, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Germanium (Ge) - Atomic Number 32
@dataclass
class Germanium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=32,
            symbol="Ge",
            name="Germanium",
            atomic_mass=72.64,
            category=ElementCategory.METALLOID.value,
            phase=Phase.SOLID.value,
            density=5.323,
            melting_point=1211.40,
            boiling_point=3106.0,
            electron_config="[Ar] 3d10 4s2 4p2",
            electronegativity=2.01,
            ionization_energy=762.0,
            isotopes=[
                Isotope(mass_number=70, symbol="Ge", atomic_mass=69.924247, abundance=20.38, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=72, symbol="Ge", atomic_mass=71.922076, abundance=27.31, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=73, symbol="Ge", atomic_mass=72.923459, abundance=7.76, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=74, symbol="Ge", atomic_mass=73.921178, abundance=36.72, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=76, symbol="Ge", atomic_mass=75.921403, abundance=7.83, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Arsenic (As) - Atomic Number 33
@dataclass
class Arsenic(Element):
    def __init__(self):
        super().__init__(
            atomic_number=33,
            symbol="As",
            name="Arsenic",
            atomic_mass=74.922,
            category=ElementCategory.METALLOID.value,
            phase=Phase.SOLID.value,
            density=5.776,
            melting_point=1090.0,
            boiling_point=887.0,
            electron_config="[Ar] 3d10 4s2 4p3",
            electronegativity=2.18,
            ionization_energy=947.0,
            isotopes=[
                Isotope(mass_number=75, symbol="As", atomic_mass=74.921596, abundance=100.0, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Selenium (Se) - Atomic Number 34
@dataclass
class Selenium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=34,
            symbol="Se",
            name="Selenium",
            atomic_mass=78.96,
            category=ElementCategory.NONMETAL.value,
            phase=Phase.SOLID.value,
            density=4.809,
            melting_point=494.0,
            boiling_point=958.0,
            electron_config="[Ar] 3d10 4s2 4p4",
            electronegativity=2.55,
            ionization_energy=941.0,
            isotopes=[
                Isotope(mass_number=74, symbol="Se", atomic_mass=73.922476, abundance=0.89, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=76, symbol="Se", atomic_mass=75.919214, abundance=9.37, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=77, symbol="Se", atomic_mass=76.919915, abundance=7.63, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=78, symbol="Se", atomic_mass=77.917310, abundance=23.77, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=80, symbol="Se", atomic_mass=79.916522, abundance=49.61, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=82, symbol="Se", atomic_mass=81.916700, abundance=8.73, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Bromine (Br) - Atomic Number 35
@dataclass
class Bromine(Element):
    def __init__(self):
        super().__init__(
            atomic_number=35,
            symbol="Br",
            name="Bromine",
            atomic_mass=79.904,
            category=ElementCategory.HALOGEN.value,
            phase=Phase.LIQUID.value,
            density=3.122,
            melting_point=265.8,
            boiling_point=332.0,
            electron_config="[Ar] 3d10 4s2 4p5",
            electronegativity=2.96,
            ionization_energy=1139.9,
            isotopes=[
                Isotope(mass_number=79, symbol="Br", atomic_mass=78.918338, abundance=50.69, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=81, symbol="Br", atomic_mass=80.916291, abundance=49.31, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Krypton (Kr) - Atomic Number 36
@dataclass
class Krypton(Element):
    def __init__(self):
        super().__init__(
            atomic_number=36,
            symbol="Kr",
            name="Krypton",
            atomic_mass=83.798,
            category=ElementCategory.NOBLE_GAS.value,
            phase=Phase.GAS.value,
            density=0.003733,
            melting_point=115.79,
            boiling_point=119.93,
            electron_config="[Ar] 3d10 4s2 4p6",
            electronegativity=3.00,
            ionization_energy=1350.8,
            isotopes=[
                Isotope(mass_number=78, symbol="Kr", atomic_mass=77.920365, abundance=0.355, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=80, symbol="Kr", atomic_mass=79.916378, abundance=2.286, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=82, symbol="Kr", atomic_mass=81.913484, abundance=11.593, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=83, symbol="Kr", atomic_mass=82.914136, abundance=11.500, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=84, symbol="Kr", atomic_mass=83.911497, abundance=56.987, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=86, symbol="Kr", atomic_mass=85.910610, abundance=17.279, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Rubidium (Rb) - Atomic Number 37
@dataclass
class Rubidium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=37,
            symbol="Rb",
            name="Rubidium",
            atomic_mass=85.468,
            category=ElementCategory.ALKALI_METAL.value,
            phase=Phase.SOLID.value,
            density=1.532,
            melting_point=312.46,
            boiling_point=961.0,
            electron_config="[Kr] 5s1",
            electronegativity=0.82,
            ionization_energy=403.0,
            isotopes=[
                Isotope(mass_number=85, symbol="Rb", atomic_mass=84.911789, abundance=72.17, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=87, symbol="Rb", atomic_mass=86.909183, abundance=27.83, decay_mode=DecayMode.BETA_MINUS.value, half_life=4.9e10),
            ]
        )


# Strontium (Sr) - Atomic Number 38
@dataclass
class Strontium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=38,
            symbol="Sr",
            name="Strontium",
            atomic_mass=87.62,
            category=ElementCategory.ALKALINE_EARTH_METAL.value,
            phase=Phase.SOLID.value,
            density=2.64,
            melting_point=1050.0,
            boiling_point=1655.0,
            electron_config="[Kr] 5s2",
            electronegativity=0.95,
            ionization_energy=549.5,
            isotopes=[
                Isotope(mass_number=84, symbol="Sr", atomic_mass=83.913420, abundance=0.56, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=86, symbol="Sr", atomic_mass=85.909262, abundance=9.86, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=87, symbol="Sr", atomic_mass=86.908879, abundance=7.00, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=88, symbol="Sr", atomic_mass=87.905614, abundance=82.58, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Yttrium (Y) - Atomic Number 39
@dataclass
class Yttrium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=39,
            symbol="Y",
            name="Yttrium",
            atomic_mass=88.906,
            category=ElementCategory.TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=4.469,
            melting_point=1799.0,
            boiling_point=3609.0,
            electron_config="[Kr] 4d1 5s2",
            electronegativity=1.22,
            ionization_energy=600.0,
            isotopes=[
                Isotope(mass_number=89, symbol="Y", atomic_mass=88.905848, abundance=100.0, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Zirconium (Zr) - Atomic Number 40
@dataclass
class Zirconium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=40,
            symbol="Zr",
            name="Zirconium",
            atomic_mass=91.224,
            category=ElementCategory.TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=6.506,
            melting_point=2128.0,
            boiling_point=4682.0,
            electron_config="[Kr] 4d2 5s2",
            electronegativity=1.33,
            ionization_energy=640.1,
            isotopes=[
                Isotope(mass_number=90, symbol="Zr", atomic_mass=89.904704, abundance=51.45, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=91, symbol="Zr", atomic_mass=90.905645, abundance=11.22, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=92, symbol="Zr", atomic_mass=91.905040, abundance=17.15, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=94, symbol="Zr", atomic_mass=93.906316, abundance=17.38, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=96, symbol="Zr", atomic_mass=95.908276, abundance=2.80, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Niobium (Nb) - Atomic Number 41
@dataclass
class Niobium(Element):
    def __init__(self):
        super().__init__(
            atomic_number=41,
            symbol="Nb",
            name="Niobium",
            atomic_mass=92.906,
            category=ElementCategory.TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=8.57,
            melting_point=2750.0,
            boiling_point=5017.0,
            electron_config="[Kr] 4d4 5s1",
            electronegativity=1.6,
            ionization_energy=652.1,
            isotopes=[
                Isotope(mass_number=93, symbol="Nb", atomic_mass=92.906378, abundance=100.0, decay_mode=DecayMode.STABLE.value),
            ]
        )


# Molybdenum (Mo) - Atomic Number 42
@dataclass
class Molybdenum(Element):
    def __init__(self):
        super().__init__(
            atomic_number=42,
            symbol="Mo",
            name="Molybdenum",
            atomic_mass=95.96,
            category=ElementCategory.TRANSITION_METAL.value,
            phase=Phase.SOLID.value,
            density=10.22,
            melting_point=2896.0,
            boiling_point=4912.0,
            electron_config="[Kr] 4d5 5s1",
            electronegativity=2.16,
            ionization_energy=684.3,
            isotopes=[
                Isotope(mass_number=92, symbol="Mo", atomic_mass=91.906810, abundance=14.53, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=94, symbol="Mo", atomic_mass=93.905088, abundance=9.15, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=95, symbol="Mo", atomic_mass=94.905841, abundance=15.84, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=96, symbol="Mo", atomic_mass=95.904679, abundance=16.67, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=97, symbol="Mo", atomic_mass=96.906021, abundance=9.60, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=98, symbol="Mo", atomic_mass=97.905408, abundance=24.39, decay_mode=DecayMode.STABLE.value),
                Isotope(mass_number=100, symbol="Mo", atomic_mass=99.907477, abundance=9.82, decay_mode=DecayMode.STABLE.value),
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
    # Period 1
    'Hydrogen', 'Helium',
    # Period 2
    'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon',
    # Period 3
    'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',
    # Period 4
    'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron',
    'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium',
    'Bromine', 'Krypton',
    # Period 5
    'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium',
    'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony',
    'Tellurium', 'Iodine', 'Xenon',
    # Period 6
    'Cesium', 'Barium', 'Lanthanum', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium',
    'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium',
    'Astatine', 'Radon',
    # Period 7
    'Francium', 'Radium', 'Actinium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium',
    'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium',
    'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson',
]
