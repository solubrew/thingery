# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Elements
	description: >
		Complete element database with all isotopes
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*

from thingery.elements.hydrogen import Hydrogen, Deuterium, Tritium
from thingery.elements.helium import Helium, Helium3, Helium4
from thingery.elements.lithium import Lithium, Lithium6, Lithium7
from thingery.elements.carbon import Carbon, Carbon12, Carbon13, Carbon14
from thingery.elements.nitrogen import Nitrogen, Nitrogen14, Nitrogen15
from thingery.elements.oxygen import Oxygen, Oxygen16, Oxygen17, Oxygen18
from thingery.elements.iron import Iron, Iron54, Iron56, Iron57, Iron60
from thingery.elements.uranium import Uranium, Uranium234, Uranium235, Uranium238


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


# ======================================Element Dictionary=============================================================||
# ====================================================================================================================||


ELEMENTS = {
    1: Hydrogen,
    2: Helium,
    3: Lithium,
    6: Carbon,
    7: Nitrogen,
    8: Oxygen,
    26: Iron,
    92: Uranium,
}


# ======================================Exports======================================================================||
# ====================================================================================================================||


__all__ = [
    # Element classes
    'Hydrogen', 'Helium', 'Lithium', 'Carbon', 'Nitrogen', 'Oxygen', 'Iron', 'Uranium',
    # Isotope classes
    'Deuterium', 'Tritium', 'Helium3', 'Helium4', 'Lithium6', 'Lithium7',
    'Carbon12', 'Carbon13', 'Carbon14', 'Nitrogen14', 'Nitrogen15',
    'Oxygen16', 'Oxygen17', 'Oxygen18',
    'Iron54', 'Iron56', 'Iron57', 'Iron60',
    'Uranium234', 'Uranium235', 'Uranium238',
    # Dictionary
    'ELEMENTS',
]
