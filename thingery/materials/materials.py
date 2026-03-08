# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name:
	description: >
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# ======================================Standard Library Modules======================================================||
from os.path import abspath, dirname, join
import datetime as dt
from dataclasses import dataclass, field
from enum import Enum

# ======================================3rd Party Library Modules=====================================================||

# ======================================Solutions Brewer Library Modules==============================================||
from condor import condor
from ogma.logma import Logma

# ====================================================================================================================||
here = join(dirname(__file__), "")  # ||
log = True
logma = Logma(__name__)

# ====================================================================================================================||
pxcfg = join(here, "../_data_", ".yaml")


class CoatingType(Enum):
    PLASTIC = "plastic"
    RUBBER = "rubber"
    POLYESTER = "polyester"
    INK = "ink"
    PAINT = "paint"
    METAL = "metal"
    UNKNOWN = "unknown"


class FinishType(Enum):
    GALVANIZED = "galvanized"
    STAINLESS = "stainless"
    BLACK = "black"
    COATED = "coated"
    ZINC = "zinc"
    BRASS = "brass"
    CHROME = "chrome"
    UNKNOWN = "unknown"


class MaterialDensity(Enum):
    """"""

    STEEL = 7.85
    STAINLESS_STEEL = 8.0
    BRASS = 8.5
    ALUMINUM = 2.7
    PLASTIC = 1.2
    UNKNOWN = 1


class MaterialType(Enum):
    STEEL = "steel"
    STAINLESS_STEEL = "stainless_steel"
    BRASS = "brass"
    ALUMINUM = "aluminum"
    PLASTIC = "plastic"
    UNKNOWN = "unknown"


class Material(object):
    """"""

    def __init__(self, name: str, finish: FinishType, density: float, type: MaterialType):
        self.name = name
        self.finish = finish
        self.density = density
        self.type = type
        self.coatings = []


# ====================================================================================================================||

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
