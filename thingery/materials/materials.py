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


# ===========================PLATINUM GROUP METALS===================================================================||
# ====================================================================================================================||


@dataclass
class Platinum(Material):
    def __init__(self):
        super().__init__(
            name="Platinum",
            formula="Pt",
            category=MaterialCategory.METAL.value,
            density=21.45,
            melting_point=2041.4,
            boiling_point=4098.0,
            hardness=4.5,
            tensile_strength=125.0,
            thermal_conductivity=71.6,
            electrical_resistivity=1.06e-7,
            properties={"precious": True, "catalytic": True, "corrosion_resistant": True}
        )


@dataclass
class Palladium(Material):
    def __init__(self):
        super().__init__(
            name="Palladium",
            formula="Pd",
            category=MaterialCategory.METAL.value,
            density=12.02,
            melting_point=1828.05,
            boiling_point=3236.0,
            hardness=4.75,
            tensile_strength=140.0,
            thermal_conductivity=71.8,
            electrical_resistivity=1.07e-7,
            properties={"catalytic": True, "hydrogen_absorption": True}
        )


@dataclass
class Rhodium(Material):
    def __init__(self):
        super().__init__(
            name="Rhodium",
            formula="Rh",
            category=MaterialCategory.METAL.value,
            density=12.41,
            melting_point=2237.0,
            boiling_point=3968.0,
            hardness=6.0,
            tensile_strength=290.0,
            thermal_conductivity=150.0,
            electrical_resistivity=4.33e-8,
            properties={"highest_reflectivity": True, "catalytic": True}
        )


# ===========================REFRACTORY METALS=======================================================================||
# ====================================================================================================================||


@dataclass
class Tungsten(Material):
    def __init__(self):
        super().__init__(
            name="Tungsten",
            formula="W",
            category=MaterialCategory.METAL.value,
            density=19.25,
            melting_point=3695.0,
            boiling_point=6203.0,
            hardness=7.5,
            tensile_strength=980.0,
            thermal_conductivity=173.0,
            electrical_resistivity=5.6e-8,
            properties={"highest_melting_point": True, "very_hard": True}
        )


@dataclass
class Tantalum(Material):
    def __init__(self):
        super().__init__(
            name="Tantalum",
            formula="Ta",
            category=MaterialCategory.METAL.value,
            density=16.654,
            melting_point=3290.0,
            boiling_point=5731.0,
            hardness=6.5,
            tensile_strength=140.0,
            thermal_conductivity=57.5,
            electrical_resistivity=1.35e-7,
            properties={"corrosion_resistant": True, "biocompatible": True}
        )


# ===========================ALKALI METALS===========================================================================||
# ====================================================================================================================||


@dataclass
class LithiumMetal(Material):
    def __init__(self):
        super().__init__(
            name="Lithium",
            formula="Li",
            category=MaterialCategory.METAL.value,
            density=0.534,
            melting_point=453.69,
            boiling_point=1560.0,
            hardness=0.6,
            thermal_conductivity=84.7,
            electrical_resistivity=9.48e-8,
            properties={"lightest_metal": True, "reactive": True}
        )


@dataclass
class SodiumMetal(Material):
    def __init__(self):
        super().__init__(
            name="Sodium",
            formula="Na",
            category=MaterialCategory.METAL.value,
            density=0.971,
            melting_point=370.87,
            boiling_point=1156.0,
            hardness=0.5,
            thermal_conductivity=142.0,
            electrical_resistivity=4.77e-8,
            properties={"highly_reactive": True, "soft": True}
        )


@dataclass
class PotassiumMetal(Material):
    def __init__(self):
        super().__init__(
            name="Potassium",
            formula="K",
            category=MaterialCategory.METAL.value,
            density=0.862,
            melting_point=336.53,
            boiling_point=1032.0,
            hardness=0.4,
            thermal_conductivity=102.5,
            electrical_resistivity=7.06e-8,
            properties={"highly_reactive": True, "soft": True}
        )


# ===========================RARE EARTH METALS=======================================================================||
# ====================================================================================================================||


@dataclass
class Neodymium(Material):
    def __init__(self):
        super().__init__(
            name="Neodymium",
            formula="Nd",
            category=MaterialCategory.METAL.value,
            density=7.01,
            melting_point=1297.0,
            boiling_point=3347.0,
            hardness=4.5,
            thermal_conductivity=16.5,
            electrical_resistivity=6.43e-7,
            properties={"magnetic": True, "used_in_permanent_magnets": True}
        )


@dataclass
class Cerium(Material):
    def __init__(self):
        super().__init__(
            name="Cerium",
            formula="Ce",
            category=MaterialCategory.METAL.value,
            density=6.77,
            melting_point=1068.0,
            boiling_point=3716.0,
            hardness=2.5,
            thermal_conductivity=11.3,
            electrical_resistivity=7.4e-7,
            properties={"most_abundant_rare_earth": True, "pyrophoric": True}
        )


# ===========================ADDITIONAL ALLOYS=======================================================================||
# ====================================================================================================================||


@dataclass
class CarbonSteel(Alloy):
    def __init__(self):
        super().__init__(
            name="Carbon Steel",
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
class ToolSteel(Alloy):
    def __init__(self):
        super().__init__(
            name="Tool Steel",
            formula="Fe+Cr+W+V+C",
            category=MaterialCategory.ALLOY.value,
            density=7.85,
            melting_point=1510.0,
            hardness=8.0,
            tensile_strength=1000.0,
            thermal_conductivity=24.0,
            electrical_resistivity=5.0e-7,
            components={"iron": 0.85, "chromium": 0.12, "tungsten": 0.025, "vanadium": 0.01}
        )


@dataclass
class Invar(Alloy):
    def __init__(self):
        super().__init__(
            name="Invar",
            formula="Fe+Ni",
            category=MaterialCategory.ALLOY.value,
            density=8.05,
            melting_point=1450.0,
            hardness=3.0,
            tensile_strength=380.0,
            thermal_conductivity=11.0,
            electrical_resistivity=7.6e-7,
            components={"iron": 0.64, "nickel": 0.36},
            properties={"low_thermal_expansion": True}
        )


# ===========================ADDITIONAL POLYMERS=====================================================================||
# ====================================================================================================================||


@dataclass
class PTFE(Polymer):
    def __init__(self):
        super().__init__(
            name="Polytetrafluoroethylene",
            formula="(C2F4)n",
            category=MaterialCategory.POLYMER.value,
            density=2.2,
            melting_point=600.0,
            hardness=0.5,
            tensile_strength=20.0,
            thermal_conductivity=0.25,
            electrical_resistivity=1.0e18,
            polymer_type="thermoplastic",
            monomer="tetrafluoroethylene",
            glass_transition_temp=115.0
        )


@dataclass
class PET(Polymer):
    def __init__(self):
        super().__init__(
            name="Polyethylene Terephthalate",
            formula="(C10H8O4)n",
            category=MaterialCategory.POLYMER.value,
            density=1.38,
            melting_point=523.0,
            hardness=2.5,
            tensile_strength=55.0,
            thermal_conductivity=0.15,
            electrical_resistivity=1.0e16,
            polymer_type="thermoplastic",
            monomer="ethylene glycol + terephthalic acid",
            glass_transition_temp=343.0
        )


@dataclass
class PMMA(Polymer):
    def __init__(self):
        super().__init__(
            name="Polymethyl Methacrylate",
            formula="(C5O2H8)n",
            category=MaterialCategory.POLYMER.value,
            density=1.18,
            melting_point=433.0,
            hardness=2.0,
            tensile_strength=50.0,
            thermal_conductivity=0.19,
            electrical_resistivity=1.0e15,
            polymer_type="thermoplastic",
            monomer="methyl methacrylate",
            glass_transition_temp=378.0,
            properties={"transparent": True, "optical": True}
        )


@dataclass
class Polycarbonate(Polymer):
    def __init__(self):
        super().__init__(
            name="Polycarbonate",
            formula="(C15H16O2)n",
            category=MaterialCategory.POLYMER.value,
            density=1.20,
            melting_point=577.0,
            hardness=2.5,
            tensile_strength=60.0,
            thermal_conductivity=0.20,
            electrical_resistivity=1.0e14,
            polymer_type="thermoplastic",
            monomer="bisphenol A + phosgene",
            glass_transition_temp=420.0,
            properties={"transparent": True, "impact_resistant": True}
        )


# ===========================ADDITIONAL CERAMICS=====================================================================||
# ====================================================================================================================||


@dataclass
class SiliconNitride(Ceramic):
    def __init__(self):
        super().__init__(
            name="Silicon Nitride",
            formula="Si3N4",
            category=MaterialCategory.CERAMIC.value,
            density=3.44,
            melting_point=2173.0,
            hardness=9.0,
            tensile_strength=600.0,
            thermal_conductivity=30.0,
            electrical_resistivity=1.0e12,
            crystal_structure="hexagonal"
        )


@dataclass
class BoronCarbide(Ceramic):
    def __init__(self):
        super().__init__(
            name="Boron Carbide",
            formula="B4C",
            category=MaterialCategory.CERAMIC.value,
            density=2.52,
            melting_point=2723.0,
            hardness=9.5,
            tensile_strength=350.0,
            thermal_conductivity=120.0,
            electrical_resistivity=1.0e5,
            crystal_structure="rhombohedral"
        )


# ===========================ADDITIONAL SEMICONDUCTORS===============================================================||
# ====================================================================================================================||


@dataclass
class GalliumNitride(Material):
    def __init__(self):
        super().__init__(
            name="Gallium Nitride",
            formula="GaN",
            category=MaterialCategory.SEMICONDUCTOR.value,
            density=6.15,
            melting_point=1973.0,
            hardness=9.0,
            tensile_strength=200.0,
            thermal_conductivity=130.0,
            electrical_resistivity=1.0e6,
            properties={"bandgap": 3.4, "type": "direct", "wide_bandgap": True}
        )


# ===========================GLASS TYPES=============================================================================||
# ====================================================================================================================||


@dataclass
class BorosilicateGlass(Material):
    def __init__(self):
        super().__init__(
            name="Borosilicate Glass",
            formula="SiO2+B2O3",
            category=MaterialCategory.GLASS.value,
            density=2.23,
            melting_point=1443.0,
            hardness=5.5,
            tensile_strength=70.0,
            thermal_conductivity=1.2,
            electrical_resistivity=1.0e14,
            properties={"low_thermal_expansion": True, "chemical_resistant": True}
        )


# ===========================MINERALS & CARBON======================================================================||
# ====================================================================================================================||


@dataclass
class Diamond(Material):
    def __init__(self):
        super().__init__(
            name="Diamond",
            formula="C",
            category=MaterialCategory.MINERAL.value,
            density=3.51,
            melting_point=4000.0,
            hardness=10.0,
            thermal_conductivity=2000.0,
            electrical_resistivity=1.0e12,
            properties={"hardest_known": True, "thermal_conductor": True, "optical": True}
        )


@dataclass
class Corundum(Material):
    def __init__(self):
        super().__init__(
            name="Corundum",
            formula="Al2O3",
            category=MaterialCategory.MINERAL.value,
            density=3.98,
            melting_point=2327.0,
            hardness=9.0,
            thermal_conductivity=30.0,
            electrical_resistivity=1.0e14,
            properties={"gem_quality": True, "abrasive": True}
        )


# ===========================BUILDING MATERIALS=====================================================================||
# ====================================================================================================================||


@dataclass
class Concrete(Material):
    def __init__(self):
        super().__init__(
            name="Concrete",
            formula="Portland Cement + Aggregate",
            category=MaterialCategory.COMPOSITE.value,
            density=2.4,
            melting_point=None,
            hardness=5.0,
            tensile_strength=3.0,
            thermal_conductivity=0.8,
            electrical_resistivity=1.0e8,
            properties={"composite": True, "versatile": True}
        )


@dataclass
class Brick(Material):
    def __init__(self):
        super().__init__(
            name="Brick",
            formula="Clay + Shale",
            category=MaterialCategory.CERAMIC.value,
            density=1.8,
            melting_point=1700.0,
            hardness=6.0,
            tensile_strength=10.0,
            thermal_conductivity=0.6,
            electrical_resistivity=1.0e6,
            properties={"durable": True, "insulating": True}
        )


# ===========================FLUIDS & SOLVENTS=======================================================================||
# ====================================================================================================================||


@dataclass
class Acetone(Material):
    def __init__(self):
        super().__init__(
            name="Acetone",
            formula="C3H6O",
            category=MaterialCategory.FLUID.value,
            density=0.784,
            melting_point=178.0,
            boiling_point=329.0,
            thermal_conductivity=0.16,
            properties={"polar_aprotic": True, "flammable": True, "solvent": True}
        )


@dataclass
class Glycerol(Material):
    def __init__(self):
        super().__init__(
            name="Glycerol",
            formula="C3H8O3",
            category=MaterialCategory.FLUID.value,
            density=1.26,
            melting_point=291.0,
            boiling_point=563.0,
            thermal_conductivity=0.29,
            properties={"hygroscopic": True, "viscous": True, "nontoxic": True}
        )


# ===========================GASES====================================================================================||
# ====================================================================================================================||


@dataclass
class HydrogenGas(Material):
    def __init__(self):
        super().__init__(
            name="Hydrogen",
            formula="H2",
            category=MaterialCategory.FLUID.value,
            density=0.00008988,
            melting_point=14.01,
            boiling_point=20.28,
            properties={"flammable": True, "lowest_density": True, "highly_reactive": True}
        )


@dataclass
class NitrogenGas(Material):
    def __init__(self):
        super().__init__(
            name="Nitrogen",
            formula="N2",
            category=MaterialCategory.FLUID.value,
            density=0.0012506,
            melting_point=63.15,
            boiling_point=77.36,
            properties={"inert": True, "cryogenic": True}
        )


# ===========================ORGANIC COMPOUNDS=======================================================================||
# ====================================================================================================================||


@dataclass
class Glucose(Material):
    def __init__(self):
        super().__init__(
            name="Glucose",
            formula="C6H12O6",
            category=MaterialCategory.CHEMICAL.value,
            density=1.54,
            melting_point=419.0,
            boiling_point=None,
            properties={"carbohydrate": True, "reducing_sugar": True}
        )


@dataclass
class SodiumHydroxide(Material):
    def __init__(self):
        super().__init__(
            name="Sodium Hydroxide",
            formula="NaOH",
            category=MaterialCategory.CHEMICAL.value,
            density=2.13,
            melting_point=591.0,
            boiling_point=1663.0,
            properties={"caustic": True, "strong_base": True, "hygroscopic": True}
        )


@dataclass
class HydrochloricAcid(Material):
    def __init__(self):
        super().__init__(
            name="Hydrochloric Acid",
            formula="HCl",
            category=MaterialCategory.CHEMICAL.value,
            density=1.18,
            melting_point=247.0,
            boiling_point=323.0,
            properties={"strong_acid": True, "corrosive": True, "strong_acid": True}
        )


# ===========================ADVANCED MATERIALS======================================================================||
# ====================================================================================================================||


@dataclass
class Graphene(Material):
    def __init__(self):
        super().__init__(
            name="Graphene",
            formula="C",
            category=MaterialCategory.NANOMATERIAL.value,
            density=2.2,
            melting_point=4000.0,
            thermal_conductivity=5000.0,
            electrical_resistivity=1.0e-6,
            properties={"single_layer": True, "extremely_strong": True, "high_conductivity": True}
        )


@dataclass
class CarbonNanotube(Material):
    def __init__(self):
        super().__init__(
            name="Carbon Nanotube",
            formula="C",
            category=MaterialCategory.NANOMATERIAL.value,
            density=1.3,
            melting_point=4000.0,
            thermal_conductivity=3000.0,
            electrical_resistivity=1.0e-5,
            properties={"cylindrical": True, "high_aspect_ratio": True, "strong": True}
        )


@dataclass
class Fullerene(Material):
    def __init__(self):
        super().__init__(
            name="Fullerene",
            formula="C60",
            category=MaterialCategory.NANOMATERIAL.value,
            density=1.65,
            melting_point=1200.0,
            properties={"spherical": True, "cage_structure": True}
        )


# ===========================EXPORTS===================================================================================||
# ====================================================================================================================||


__all__ = [
    # Metals
    'Iron', 'Copper', 'Aluminum', 'Gold', 'Silver', 'Titanium', 'Magnesium', 'Zinc', 'Nickel', 'Lead',
    'Platinum', 'Palladium', 'Rhodium', 'Iridium', 'Osmium', 'Ruthenium', 'Chromium', 'Manganese',
    'Vanadium', 'Cobalt', 'Tungsten', 'Molybdenum', 'Tantalum', 'Niobium', 'Zirconium', 'Hafnium',
    'Scandium', 'Yttrium', 'Lanthanum', 'Cerium', 'Neodymium', 'Samarium', 'Gadolinium', 'Dysprosium',
    # Alkali Metals
    'Lithium', 'Sodium', 'Potassium', 'Rubidium', 'Cesium', 'Francium',
    # Alkaline Earth Metals
    'Beryllium', 'Calcium', 'Strontium', 'Barium', 'Radium',
    # Post-Transition Metals
    'Indium', 'Tin', 'Thallium', 'LeadMat', 'Bismuth',
    # Metalloids
    'Boron', 'Silicon', 'GermaniumMat', 'Arsenic', 'Antimony', 'Tellurium',
    # Nonmetals
    'CarbonNonmetal', 'Nitrogen', 'Oxygen', 'Phosphorus', 'Sulfur', 'Selenium',
    # Halogens
    'Fluorine', 'Chlorine', 'Bromine', 'Iodine', 'Astatine',
    # Noble Gases
    'Helium', 'Neon', 'Argon', 'Krypton', 'Xenon', 'Radon',
    # Alloys
    'Steel', 'StainlessSteel', 'Brass', 'Bronze', 'CastIron',
    'CarbonSteel', 'ToolSteel', 'NickelSilver', 'Solder', 'Pewter', 'Duralumin', 'Invar', 'Kovar',
    # Polymers
    'Polyethylene', 'Polypropylene', 'Polystyrene', 'PolyvinylChloride', 'Nylon',
    'PTFE', 'PET', 'PMMA', 'PVC', 'ABS', 'Polycarbonate', 'PPS', 'PEEK', 'PVDF',
    # Ceramics
    'Alumina', 'Zirconia', 'SiliconCarbide', 'SiliconNitride', 'BoronCarbide', 'TitaniumCarbide',
    'AluminumNitride', 'TungstenCarbide', 'MolybdenumDisilicide',
    # Semiconductors
    'SiliconSemiconductor', 'Germanium', 'GalliumArsenide', 'GalliumNitride', 'IndiumPhosphide', 'CadmiumTelluride',
    # Glass
    'Glass', 'BorosilicateGlass', 'QuartzGlass', 'LeadGlass',
    # Composites
    'CarbonFiberComposite', 'GlassFiberComposite', 'KevlarComposite', 'CFRP', 'GFRP',
    # Minerals
    'Quartz', 'Graphite', 'Diamond', 'Corundum', 'Topaz', 'Fluorite', 'Mica', 'Talc', 'Clay', 'Sand',
    # Fluids
    'Water', 'Ethanol', 'Acetone', 'Benzene', 'Toluene', 'Methanol', 'Isopropanol', 'Glycerol',
    'Mercury', 'Bromine', 'Gallium',
    # Gases
    'HydrogenGas', 'NitrogenGas', 'OxygenGas', 'ArgonGas', 'HeliumGas', 'CarbonDioxide', 'Methane', 'Ammonia',
    # Organic Compounds
    'Glucose', 'Sucrose', 'AceticAcid', 'SodiumHydroxide', 'SodiumChloride', 'HydrochloricAcid',
    'SulfuricAcid', 'NitricAcid', 'AcetoneCompound', 'Chloroform', 'Dichloromethane', 'Hexane',
    # Building Materials
    'Concrete', 'Brick', 'Cement', 'Mortite', 'Asphalt', 'Wood', 'Granite', 'Marble', 'Limestone',
    # Advanced Materials
    'Graphene', 'CarbonNanotube', 'Fullerene', 'MXene', 'Perovskite', 'Superconductor',
]
