# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Materials
	description: >
		Complete materials database - metals, alloys, polymers, ceramics, semiconductors
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from dataclasses import dataclass, field
from typing import Dict, Optional
from thingery.models import Material, Alloy, Polymer, Ceramic, MaterialCategory


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


# ===========================METALS=================================================================================||
# ====================================================================================================================||


@dataclass
class Iron(Material):
    def __init__(self):
        super().__init__(
            name="Iron",
            formula="Fe",
            category=MaterialCategory.METAL.value,
            density=7.874,
            melting_point=1811.0,
            boiling_point=3134.0,
            hardness=4.0,
            tensile_strength=380.0,
            thermal_conductivity=80.4,
            electrical_resistivity=9.71e-8,
            properties={"magnetic": True, "corrosion_prone": True}
        )


@dataclass
class Copper(Material):
    def __init__(self):
        super().__init__(
            name="Copper",
            formula="Cu",
            category=MaterialCategory.METAL.value,
            density=8.96,
            melting_point=1357.77,
            boiling_point=2835.0,
            hardness=3.0,
            tensile_strength=220.0,
            thermal_conductivity=401.0,
            electrical_resistivity=1.68e-8,
            properties={"electrical_conductivity": "excellent", "malleable": True}
        )


@dataclass
class Aluminum(Material):
    def __init__(self):
        super().__init__(
            name="Aluminum",
            formula="Al",
            category=MaterialCategory.METAL.value,
            density=2.698,
            melting_point=933.47,
            boiling_point=2792.0,
            hardness=2.75,
            tensile_strength=90.0,
            thermal_conductivity=235.0,
            electrical_resistivity=2.65e-8,
            properties={"lightweight": True, "corrosion_resistant": True}
        )


@dataclass
class Gold(Material):
    def __init__(self):
        super().__init__(
            name="Gold",
            formula="Au",
            category=MaterialCategory.METAL.value,
            density=19.282,
            melting_point=1337.33,
            boiling_point=3129.0,
            hardness=2.5,
            tensile_strength=100.0,
            thermal_conductivity=317.0,
            electrical_resistivity=2.44e-8,
            properties={"corrosion_resistant": True, "malleable": True, "precious": True}
        )


@dataclass
class Silver(Material):
    def __init__(self):
        super().__init__(
            name="Silver",
            formula="Ag",
            category=MaterialCategory.METAL.value,
            density=10.501,
            melting_point=1234.93,
            boiling_point=2435.0,
            hardness=2.5,
            tensile_strength=140.0,
            thermal_conductivity=429.0,
            electrical_resistivity=1.59e-8,
            properties={"highest_electrical_conductivity": True, "precious": True}
        )


@dataclass
class Titanium(Material):
    def __init__(self):
        super().__init__(
            name="Titanium",
            formula="Ti",
            category=MaterialCategory.METAL.value,
            density=4.54,
            melting_point=1941.0,
            boiling_point=3560.0,
            hardness=6.0,
            tensile_strength=240.0,
            thermal_conductivity=21.9,
            electrical_resistivity=4.20e-7,
            properties={"high_strength_to_weight": True, "corrosion_resistant": True}
        )


@dataclass
class Magnesium(Material):
    def __init__(self):
        super().__init__(
            name="Magnesium",
            formula="Mg",
            category=MaterialCategory.METAL.value,
            density=1.738,
            melting_point=923.0,
            boiling_point=1363.0,
            hardness=2.5,
            tensile_strength=90.0,
            thermal_conductivity=156.0,
            electrical_resistivity=4.45e-8,
            properties={"lightest_structural_metal": True, "flammable": True}
        )


@dataclass
class Zinc(Material):
    def __init__(self):
        super().__init__(
            name="Zinc",
            formula="Zn",
            category=MaterialCategory.METAL.value,
            density=7.134,
            melting_point=692.88,
            boiling_point=1180.0,
            hardness=2.5,
            tensile_strength=110.0,
            thermal_conductivity=116.0,
            electrical_resistivity=5.90e-8,
            properties={"corrosion_resistant": True, "galvanizing": True}
        )


@dataclass
class Nickel(Material):
    def __init__(self):
        super().__init__(
            name="Nickel",
            formula="Ni",
            category=MaterialCategory.METAL.value,
            density=8.912,
            melting_point=1728.0,
            boiling_point=3186.0,
            hardness=4.0,
            tensile_strength=450.0,
            thermal_conductivity=90.9,
            electrical_resistivity=6.99e-8,
            properties={"magnetic": True, "corrosion_resistant": True}
        )


@dataclass
class Lead(Material):
    def __init__(self):
        super().__init__(
            name="Lead",
            formula="Pb",
            category=MaterialCategory.METAL.value,
            density=11.342,
            melting_point=600.61,
            boiling_point=2022.0,
            hardness=1.5,
            tensile_strength=15.0,
            thermal_conductivity=35.3,
            electrical_resistivity=2.08e-7,
            properties={"toxic": True, "dense": True, "soft": True}
        )


# ===========================ALLOYS==================================================================================||
# ====================================================================================================================||


@dataclass
class Steel(Alloy):
    def __init__(self):
        super().__init__(
            name="Steel",
            formula="Fe+C",
            category=MaterialCategory.ALLOY.value,
            density=7.85,
            melting_point=1510.0,
            hardness=4.0,
            tensile_strength=515.0,
            thermal_conductivity=50.0,
            electrical_resistivity=1.5e-7,
            components={"iron": 0.98, "carbon": 0.02}
        )


@dataclass
class StainlessSteel(Alloy):
    def __init__(self):
        super().__init__(
            name="Stainless Steel",
            formula="Fe+Cr+Ni",
            category=MaterialCategory.ALLOY.value,
            density=8.0,
            melting_point=1725.0,
            hardness=5.0,
            tensile_strength=620.0,
            thermal_conductivity=16.0,
            electrical_resistivity=7.2e-7,
            components={"iron": 0.74, "chromium": 0.18, "nickel": 0.08}
        )


@dataclass
class Brass(Alloy):
    def __init__(self):
        super().__init__(
            name="Brass",
            formula="Cu+Zn",
            category=MaterialCategory.ALLOY.value,
            density=8.5,
            melting_point=1190.0,
            hardness=3.0,
            tensile_strength=385.0,
            thermal_conductivity=120.0,
            electrical_resistivity=6.4e-8,
            components={"copper": 0.70, "zinc": 0.30}
        )


@dataclass
class Bronze(Alloy):
    def __init__(self):
        super().__init__(
            name="Bronze",
            formula="Cu+Sn",
            category=MaterialCategory.ALLOY.value,
            density=8.7,
            melting_point=1200.0,
            hardness=3.5,
            tensile_strength=350.0,
            thermal_conductivity=42.0,
            electrical_resistivity=1.0e-7,
            components={"copper": 0.90, "tin": 0.10}
        )


@dataclass
class CastIron(Alloy):
    def __init__(self):
        super().__init__(
            name="Cast Iron",
            formula="Fe+Si+C",
            category=MaterialCategory.ALLOY.value,
            density=7.15,
            melting_point=1450.0,
            hardness=4.5,
            tensile_strength=180.0,
            thermal_conductivity=46.0,
            electrical_resistivity=5.0e-7,
            components={"iron": 0.95, "carbon": 0.03, "silicon": 0.02}
        )


# ===========================POLYMERS================================================================================||
# ====================================================================================================================||


@dataclass
class Polyethylene(Polymer):
    def __init__(self):
        super().__init__(
            name="Polyethylene",
            formula="(C2H4)n",
            category=MaterialCategory.POLYMER.value,
            density=0.91,
            melting_point=394.0,
            hardness=0.5,
            tensile_strength=8.0,
            thermal_conductivity=0.33,
            electrical_resistivity=1.0e16,
            polymer_type="thermoplastic",
            monomer="ethylene",
            glass_transition_temp=148.0
        )


@dataclass
class Polypropylene(Polymer):
    def __init__(self):
        super().__init__(
            name="Polypropylene",
            formula="(C3H6)n",
            category=MaterialCategory.POLYMER.value,
            density=0.90,
            melting_point=448.0,
            hardness=0.7,
            tensile_strength=25.0,
            thermal_conductivity=0.17,
            electrical_resistivity=1.0e17,
            polymer_type="thermoplastic",
            monomer="propylene",
            glass_transition_temp=253.0
        )


@dataclass
class Polystyrene(Polymer):
    def __init__(self):
        super().__init__(
            name="Polystyrene",
            formula="(C8H8)n",
            category=MaterialCategory.POLYMER.value,
            density=1.05,
            melting_point=513.0,
            hardness=1.5,
            tensile_strength=30.0,
            thermal_conductivity=0.08,
            electrical_resistivity=1.0e18,
            polymer_type="thermoplastic",
            monomer="styrene",
            glass_transition_temp=373.0
        )


@dataclass
class PolyvinylChloride(Polymer):
    def __init__(self):
        super().__init__(
            name="Polyvinyl Chloride",
            formula="(C2H3Cl)n",
            category=MaterialCategory.POLYMER.value,
            density=1.30,
            melting_point=532.0,
            hardness=1.5,
            tensile_strength=40.0,
            thermal_conductivity=0.16,
            electrical_resistivity=1.0e14,
            polymer_type="thermoplastic",
            monomer="vinyl chloride",
            glass_transition_temp=354.0
        )


@dataclass
class Nylon(Polymer):
    def __init__(self):
        super().__init__(
            name="Nylon",
            formula="(C12H22O2N2)n",
            category=MaterialCategory.POLYMER.value,
            density=1.14,
            melting_point=533.0,
            hardness=2.0,
            tensile_strength=60.0,
            thermal_conductivity=0.25,
            electrical_resistivity=1.0e13,
            polymer_type="thermoplastic",
            monomer="adipic acid + hexamethylenediamine",
            glass_transition_temp=343.0
        )


# ===========================CERAMICS=================================================================================||
# ====================================================================================================================||


@dataclass
class Alumina(Ceramic):
    def __init__(self):
        super().__init__(
            name="Aluminum Oxide (Alumina)",
            formula="Al2O3",
            category=MaterialCategory.CERAMIC.value,
            density=3.95,
            melting_point=2327.0,
            hardness=9.0,
            tensile_strength=275.0,
            thermal_conductivity=30.0,
            electrical_resistivity=1.0e14,
            crystal_structure="hexagonal"
        )


@dataclass
class Zirconia(Ceramic):
    def __init__(self):
        super().__init__(
            name="Zirconium Oxide",
            formula="ZrO2",
            category=MaterialCategory.CERAMIC.value,
            density=5.68,
            melting_point=2988.0,
            hardness=8.5,
            tensile_strength=800.0,
            thermal_conductivity=2.0,
            electrical_resistivity=1.0e10,
            crystal_structure="monoclinic"
        )


@dataclass
class SiliconCarbide(Ceramic):
    def __init__(self):
        super().__init__(
            name="Silicon Carbide",
            formula="SiC",
            category=MaterialCategory.CERAMIC.value,
            density=3.21,
            melting_point=3000.0,
            hardness=9.5,
            tensile_strength=400.0,
            thermal_conductivity=120.0,
            electrical_resistivity=1.0e3,
            crystal_structure="cubic"
        )


# ===========================SEMICONDUCTORS===========================================================================||
# ====================================================================================================================||


@dataclass
class SiliconSemiconductor(Material):
    def __init__(self):
        super().__init__(
            name="Silicon",
            formula="Si",
            category=MaterialCategory.SEMICONDUCTOR.value,
            density=2.3296,
            melting_point=1687.0,
            boiling_point=3538.0,
            hardness=6.5,
            tensile_strength=100.0,
            thermal_conductivity=148.0,
            electrical_resistivity=6.40e2,
            properties={"bandgap": 1.12, "type": "indirect"}
        )


@dataclass
class Germanium(Material):
    def __init__(self):
        super().__init__(
            name="Germanium",
            formula="Ge",
            category=MaterialCategory.SEMICONDUCTOR.value,
            density=5.323,
            melting_point=1211.40,
            boiling_point=3106.0,
            hardness=6.0,
            tensile_strength=100.0,
            thermal_conductivity=59.9,
            electrical_resistivity=4.60e1,
            properties={"bandgap": 0.66, "type": "indirect"}
        )


@dataclass
class GalliumArsenide(Material):
    def __init__(self):
        super().__init__(
            name="Gallium Arsenide",
            formula="GaAs",
            category=MaterialCategory.SEMICONDUCTOR.value,
            density=5.318,
            melting_point=1511.0,
            boiling_point=1730.0,
            hardness=7.5,
            tensile_strength=125.0,
            thermal_conductivity=45.0,
            electrical_resistivity=1.0e7,
            properties={"bandgap": 1.42, "type": "direct"}
        )


# ===========================GLASSES=================================================================================||
# ====================================================================================================================||


@dataclass
class Glass(Material):
    def __init__(self):
        super().__init__(
            name="Soda-Lime Glass",
            formula="SiO2+Na2O+CaO",
            category=MaterialCategory.GLASS.value,
            density=2.5,
            melting_point=1400.0,
            hardness=5.5,
            tensile_strength=70.0,
            thermal_conductivity=1.0,
            electrical_resistivity=1.0e12,
            properties={"transparent": True, "brittle": True}
        )


# ===========================COMPOSITES===============================================================================||
# ====================================================================================================================||


@dataclass
class CarbonFiberComposite(Material):
    def __init__(self):
        super().__init__(
            name="Carbon Fiber Reinforced Polymer",
            formula="CFRP",
            category=MaterialCategory.COMPOSITE.value,
            density=1.6,
            tensile_strength=600.0,
            thermal_conductivity=5.0,
            properties={"anisotropic": True, "high_strength_to_weight": True}
        )


# ===========================MINERALS=================================================================================||
# ====================================================================================================================||


@dataclass
class Quartz(Material):
    def __init__(self):
        super().__init__(
            name="Quartz",
            formula="SiO2",
            category=MaterialCategory.MINERAL.value,
            density=2.65,
            melting_point=1880.0,
            hardness=7.0,
            properties={"piezoelectric": True, "transparent": True}
        )


@dataclass
class Graphite(Material):
    def __init__(self):
        super().__init__(
            name="Graphite",
            formula="C",
            category=MaterialCategory.MINERAL.value,
            density=2.26,
            melting_point=3800.0,
            hardness=1.5,
            thermal_conductivity=119.0,
            properties={"lubricious": True, "conductive": True, "anisotropic": True}
        )


# ===========================FLUIDS===================================================================================||
# ====================================================================================================================||


@dataclass
class Water(Material):
    def __init__(self):
        super().__init__(
            name="Water",
            formula="H2O",
            category=MaterialCategory.FLUID.value,
            density=1.0,
            melting_point=273.15,
            boiling_point=373.15,
            thermal_conductivity=0.606,
            properties={"polar": True, "universal_solvent": True}
        )


@dataclass
class Ethanol(Material):
    def __init__(self):
        super().__init__(
            name="Ethanol",
            formula="C2H5OH",
            category=MaterialCategory.FLUID.value,
            density=0.789,
            melting_point=159.0,
            boiling_point=351.0,
            thermal_conductivity=0.169,
            properties={"polar": True, "flammable": True}
        )


# ===========================EXPORTS===================================================================================||
# ====================================================================================================================||


__all__ = [
    # Metals
    'Iron', 'Copper', 'Aluminum', 'Gold', 'Silver', 'Titanium', 'Magnesium', 'Zinc', 'Nickel', 'Lead',
    # Alloys
    'Steel', 'StainlessSteel', 'Brass', 'Bronze', 'CastIron',
    # Polymers
    'Polyethylene', 'Polypropylene', 'Polystyrene', 'PolyvinylChloride', 'Nylon',
    # Ceramics
    'Alumina', 'Zirconia', 'SiliconCarbide',
    # Semiconductors
    'SiliconSemiconductor', 'Germanium', 'GalliumArsenide',
    # Glass
    'Glass',
    # Composites
    'CarbonFiberComposite',
    # Minerals
    'Quartz', 'Graphite',
    # Fluids
    'Water', 'Ethanol',
]
